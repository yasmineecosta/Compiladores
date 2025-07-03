import tkinter as tk
from tkinter import ttk, filedialog, scrolledtext, messagebox
import subprocess
import os
import sys
import threading
import queue


# --- Funções de Backend (sem alterações) ---

def run_compiler(file_path):
    """Executa o processo principal de compilação."""
    base_name = os.path.splitext(os.path.basename(file_path))[0]
    tac_file_path = f"{base_name}.tac"
    python_executable = sys.executable

    process = subprocess.run(
        [python_executable, "main.py", file_path],
        capture_output=True,
        text=True,
        encoding='utf-8',
        errors='replace'
    )

    full_output = (process.stdout or "") + (process.stderr or "")

    if process.returncode != 0 or not os.path.exists(tac_file_path):
        return None, full_output

    return tac_file_path, full_output


def run_tac_executor(tac_file_path):
    """Executa o interpretador TAC."""
    if not os.path.exists(tac_file_path):
        return f"ERRO: Arquivo TAC '{tac_file_path}' não foi encontrado."

    python_executable = sys.executable

    process = subprocess.Popen(
        [python_executable, "-u", "tac_executor.py", tac_file_path],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        encoding='utf-8',
        errors='replace'
    )
    return process


# --- Classes da Interface Gráfica ---

class TextLineNumbers(tk.Canvas):
    def __init__(self, *args, **kwargs):
        tk.Canvas.__init__(self, *args, **kwargs)
        self.textwidget = None

    def attach(self, text_widget):
        self.textwidget = text_widget

    def redraw(self, *args):
        self.delete("all")
        i = self.textwidget.index("@0,0")
        while True:
            dline = self.textwidget.dlineinfo(i)
            if dline is None:
                break
            y = dline[1]
            linenum = str(i).split(".")[0]
            self.create_text(38, y, anchor="ne", text=linenum, fill="#6c757d", font=("Consolas", 10))
            i = self.textwidget.index(f"{i}+1line")


class CustomText(tk.Text):
    def __init__(self, *args, **kwargs):
        tk.Text.__init__(self, *args, **kwargs)
        self._orig = self._w + "_orig"
        self.tk.call("rename", self._w, self._orig)
        self.tk.createcommand(self._w, self._proxy)

    def _proxy(self, *args):
        try:
            command = (self._orig,) + args
            result = self.tk.call(command)
            if any(a in args for a in ("insert", "delete", "replace")):
                self.event_generate("<<TextModified>>")
            return result
        except tk.TclError:
            return ""


class CompilerIDE:
    def __init__(self, root):
        self.root = root
        self.root.title("Javython IDE")
        self.root.geometry("900x700")

        self.current_file_path = None
        self.last_tac_file = None
        self.proc = None
        self.output_queue = queue.Queue()

        self.create_menu()

        main_pane = tk.PanedWindow(root, orient=tk.HORIZONTAL, sashrelief=tk.RAISED)
        main_pane.pack(fill=tk.BOTH, expand=True)

        left_pane = ttk.Notebook(main_pane)
        # CORREÇÃO: Removido o parâmetro 'weight'
        main_pane.add(left_pane)
        self.create_editor_tab(left_pane)
        self.create_explorer_tab(left_pane)

        right_pane = tk.Frame(main_pane, padx=5, pady=5)
        # CORREÇÃO: Removido o parâmetro 'weight'
        main_pane.add(right_pane)

        tk.Label(right_pane, text="Saída do Compilador e Execução:").pack(anchor='w')
        self.output_text = scrolledtext.ScrolledText(right_pane, wrap=tk.WORD)
        self.output_text.pack(fill=tk.BOTH, expand=True)
        self.output_text.config(state=tk.DISABLED, bg="#1e1e1e", fg="#d4d4d4", font=("Consolas", 10))

        input_frame = tk.Frame(right_pane, pady=5)
        input_frame.pack(fill=tk.X, side=tk.BOTTOM)
        tk.Label(input_frame, text="Entrada:").pack(side=tk.LEFT)
        self.input_entry = tk.Entry(input_frame)
        self.input_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)
        self.send_button = tk.Button(input_frame, text="Enviar", command=self.send_input_to_process)
        self.send_button.pack(side=tk.LEFT)
        self.input_entry.bind("<Return>", lambda event: self.send_input_to_process())
        self.toggle_input(False)

        self.root.after(100, self.process_output_queue)

    def create_menu(self):
        menu_bar = tk.Menu(self.root)
        self.root.config(menu=menu_bar)
        file_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Arquivo", menu=file_menu)
        file_menu.add_command(label="Novo Arquivo", command=self.new_file)
        file_menu.add_command(label="Salvar", command=self.save_file)
        file_menu.add_command(label="Salvar Como...", command=self.save_file_as)
        file_menu.add_separator()
        file_menu.add_command(label="Sair", command=self.root.quit)

    def create_editor_tab(self, notebook):
        editor_pane = ttk.Frame(notebook)
        notebook.add(editor_pane, text='Editor')

        button_frame = tk.Frame(editor_pane)
        button_frame.pack(fill=tk.X, pady=5)
        self.compile_button = tk.Button(button_frame, text="Compilar", command=self.compile_code)
        self.compile_button.pack(side=tk.LEFT, padx=5)
        self.execute_button = tk.Button(button_frame, text="Executar TAC", command=self.execute_tac, state=tk.DISABLED)
        self.execute_button.pack(side=tk.LEFT, padx=5)

        editor_area = tk.Frame(editor_pane)
        editor_area.pack(fill=tk.BOTH, expand=True)
        self.linenumbers = TextLineNumbers(editor_area, width=40, bg='#f8f9fa')
        self.linenumbers.pack(side=tk.LEFT, fill=tk.Y)
        self.editor_text = CustomText(editor_area, wrap=tk.WORD, undo=True, font=("Consolas", 10))
        self.editor_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.linenumbers.attach(self.editor_text)

        events = ["<<TextModified>>", "<Configure>", "<KeyRelease>", "<MouseWheel>"]
        for event in events:
            self.editor_text.bind(event, self._on_text_modify)

        # Preenche com o código de exemplo do usuário
        self.prefill_editor_with_example()

    def create_explorer_tab(self, notebook):
        explorer_pane = ttk.Frame(notebook)
        notebook.add(explorer_pane, text='Explorador de Arquivos')
        self.file_tree = ttk.Treeview(explorer_pane)
        self.file_tree.pack(side=tk.LEFT, fill="both", expand=True)
        scrollbar = ttk.Scrollbar(explorer_pane, orient="vertical", command=self.file_tree.yview)
        scrollbar.pack(side=tk.RIGHT, fill="y")
        self.file_tree.configure(yscrollcommand=scrollbar.set)
        self.file_tree.bind("<Double-1>", self.on_file_select)
        refresh_button = tk.Button(explorer_pane, text="Atualizar", command=self.populate_file_explorer)
        refresh_button.pack(side=tk.BOTTOM, fill=tk.X, pady=5)
        self.populate_file_explorer()

    def populate_file_explorer(self):
        for i in self.file_tree.get_children():
            self.file_tree.delete(i)
        path = os.getcwd()
        for item in sorted(os.listdir(path)):
            icon = "📁" if os.path.isdir(item) else "📄"
            self.file_tree.insert("", "end", text=f" {icon} {item}", iid=item)

    def on_file_select(self, event):
        selection = self.file_tree.selection()
        if not selection: return
        item_id = selection[0]
        # Remove o ícone do nome do arquivo
        if item_id.startswith("📄 ") or item_id.startswith("📁 "):
            item_id = item_id[2:]

        full_path = os.path.join(os.getcwd(), item_id)
        if os.path.isfile(full_path) and item_id.endswith(".jy"):
            try:
                with open(full_path, "r", encoding="utf-8") as f:
                    content = f.read()
                self.new_file()
                self.editor_text.insert("1.0", content)
                self.current_file_path = full_path
                self.root.title(f"Javython IDE - {os.path.basename(full_path)}")
                self.notebook.select(0)
            except Exception as e:
                messagebox.showerror("Erro ao Abrir", f"Não foi possível ler o arquivo:\n{e}")

    def new_file(self):
        self.editor_text.delete("1.0", tk.END)
        self.current_file_path = None
        self.last_tac_file = None
        self.execute_button.config(state=tk.DISABLED)
        self.root.title("Javython IDE - Novo Arquivo")

    def save_file_as(self):
        path = filedialog.asksaveasfilename(initialfile="novo.jy", defaultextension=".jy",
                                            filetypes=[("Javython files", "*.jy"), ("All files", "*.*")])
        if path:
            self.current_file_path = path
            self.root.title(f"Javython IDE - {os.path.basename(path)}")
            return self.save_file()
        return False

    def save_file(self):
        if not self.current_file_path:
            return self.save_file_as()
        try:
            with open(self.current_file_path, "w", encoding="utf-8") as f:
                f.write(self.editor_text.get("1.0", tk.END).strip())
            self.log_output(f"✔️ Arquivo salvo como '{os.path.basename(self.current_file_path)}'\n")
            return True
        except Exception as e:
            messagebox.showerror("Erro ao Salvar", f"Não foi possível salvar o arquivo:\n{e}")
            return False

    def log_output(self, message):
        self.output_text.config(state=tk.NORMAL)
        self.output_text.insert(tk.END, message)
        self.output_text.see(tk.END)
        self.output_text.config(state=tk.DISABLED)

    def process_output_queue(self):
        try:
            while True: self.log_output(self.output_queue.get_nowait())
        except queue.Empty:
            pass
        self.root.after(100, self.process_output_queue)

    def compile_code(self):
        self.log_output("\n" + "=" * 20 + " COMPILAÇÃO " + "=" * 20 + "\n")
        if not self.save_file(): return
        self.compile_button.config(state=tk.DISABLED)
        self.execute_button.config(state=tk.DISABLED)
        self.last_tac_file = None
        threading.Thread(target=self._compile_backend, daemon=True).start()

    def _compile_backend(self):
        try:
            tac_file, compile_log = run_compiler(self.current_file_path)
            self.output_queue.put(compile_log + "\n")
            if tac_file:
                self.last_tac_file = tac_file
                self.output_queue.put(f"✔️ Compilação bem-sucedida! Arquivo '{os.path.basename(tac_file)}' gerado.\n")
                self.root.after(0, self.execute_button.config, {'state': tk.NORMAL})
            else:
                self.output_queue.put("--- FALHA NA COMPILAÇÃO. Verifique os erros acima. ---\n")
        finally:
            self.root.after(0, self.compile_button.config, {'state': tk.NORMAL})

    def execute_tac(self):
        if not self.last_tac_file: return
        self.log_output("\n" + "=" * 20 + " EXECUÇÃO " + "=" * 20 + "\n")
        self.toggle_buttons(False)
        threading.Thread(target=self._execute_backend_tac, daemon=True).start()

    def _execute_backend_tac(self):
        try:
            self.proc = run_tac_executor(self.last_tac_file)
            threading.Thread(target=self.read_from_process, args=(self.proc.stdout,), daemon=True).start()
            threading.Thread(target=self.read_from_process, args=(self.proc.stderr,), daemon=True).start()
        except Exception as e:
            self.output_queue.put(f"\n--- ERRO AO INICIAR EXECUÇÃO ---\n{type(e).__name__}: {e}\n")
            self.root.after(0, self.toggle_buttons, True)

    def read_from_process(self, stream):
        for line in iter(stream.readline, ''):
            if ">>INPUT>>" in line:
                self.root.after(0, self.toggle_input, True)
            else:
                self.output_queue.put(line)
        stream.close()
        self.root.after(100, self.check_process_end)

    def check_process_end(self):
        if self.proc and self.proc.poll() is not None:
            self.output_queue.put("\n--- Fim da Execução ---\n")
            self.root.after(0, self.toggle_buttons, True)
            self.root.after(0, self.toggle_input, False)
            self.proc = None

    def send_input_to_process(self):
        if self.proc and self.proc.poll() is None:
            input_val = self.input_entry.get()
            self.proc.stdin.write(input_val + '\n')
            self.proc.stdin.flush()
            self.log_output(f"{input_val}\n")
            self.input_entry.delete(0, tk.END)
            self.toggle_input(False)

    def toggle_buttons(self, enabled):
        state = tk.NORMAL if enabled else tk.DISABLED
        self.compile_button.config(state=state)
        # Só reabilita o botão de executar se ainda tivermos um .tac válido
        if enabled and self.last_tac_file:
            self.execute_button.config(state=tk.NORMAL)
        else:
            self.execute_button.config(state=tk.DISABLED)

    def toggle_input(self, enabled=False):
        state = tk.NORMAL if enabled else tk.DISABLED
        self.input_entry.config(state=state)
        self.send_button.config(state=state)
        if enabled: self.input_entry.focus()

    def _on_text_modify(self, event=None):
        self.linenumbers.redraw()

    def prefill_editor_with_example(self):
        example_code = """program: Exemplo1;

decIds:
    i : int;

int fatorial (int fat){
    if (fat > 1){
        return fat * fatorial(fat - 1);
    } else {
        return 1;
    }
}

void mostrarMedia (int v1, int v2){
    decIds:
        x : real;

    x = (v1+v2)/2.0; // Dividir por 2.0 para garantir resultado real
    print("Resultado: ", x);
}

main:
    decIds:
        numero : int;
        n1, n2, i : int;

    print("Programa Fatorial Digite o valor?");
    input(numero);
    print("O fatorial e: ", fatorial(numero));

    print("Programa Media Digite os valores?");
    input(n1, n2);
    mostrarMedia(n1,n2);

    for(i=0; i < 10 ;i++){
        print("Teste for.");
    }
end
"""
        self.editor_text.insert("1.0", example_code)


if __name__ == '__main__':
    if getattr(sys, 'frozen', False):
        application_path = os.path.dirname(sys.executable)
    else:
        application_path = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(application_path)

    root = tk.Tk()
    app = CompilerIDE(root)
    root.mainloop()