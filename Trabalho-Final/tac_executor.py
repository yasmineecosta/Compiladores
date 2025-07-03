# tac_executor.py (Versão Definitiva com Lógica de Execução Simplificada)

import sys
from antlr4 import *
from JavythonLexer import JavythonLexer
from JavythonParser import JavythonParser
from analisador_semantico import AnalisadorSemantico


class TACExecutor:
    def __init__(self, analisador: AnalisadorSemantico):
        self.memory_stack = [{}]
        self.instructions = []
        self.pc = 0
        self.labels = {}
        self.call_stack = []
        self.param_stack = []
        self.tabela_simbolos = analisador.tabela

    def current_memory(self):
        return self.memory_stack[-1]

    def _set_value(self, name, value):
        for frame in reversed(self.memory_stack):
            if name in frame:
                frame[name] = value
                return
        self.current_memory()[name] = value

    def _get_value(self, name):
        try:
            return int(name)
        except ValueError:
            try:
                return float(name)
            except ValueError:
                if name == 'true': return True
                if name == 'false': return False
                if name.startswith('"') and name.endswith('"'): return name[1:-1]
        for frame in reversed(self.memory_stack):
            if name in frame:
                return frame[name]
        return None

    def _scan_labels(self):
        self.labels = {}
        for i, instruction in enumerate(self.instructions):
            parts = instruction.strip().split()
            if parts and parts[0] == 'label':
                self.labels[parts[1]] = i

    def run(self, instructions: list):
        self.instructions = instructions
        self._scan_labels()
        self.pc = self.labels.get('main_entry', 0)

        while 0 <= self.pc < len(self.instructions):
            instruction = self.instructions[self.pc].strip()
            if not instruction:
                self.pc += 1
                continue

            next_pc = self.pc + 1
            parts = instruction.split()
            command = parts[0]

            # --- LÓGICA DE PARSING E EXECUÇÃO REFEITA E SIMPLIFICADA ---
            if command == 'label':
                pass  # Nenhuma ação

            elif len(parts) > 1 and parts[1] == '=':  # Trata `dest = ...`
                dest = parts[0]
                expr_parts = parts[2:]

                if expr_parts[0] == 'call':  # Caso: x = call func, n
                    func_name, _ = expr_parts[1].split(',')
                    self.call_stack.append({'pc': next_pc, 'dest': dest})
                    new_frame = {}
                    simbolo_metodo = self.tabela_simbolos.buscar(func_name)
                    if simbolo_metodo and simbolo_metodo.parametros:
                        param_names = [p[1] for p in simbolo_metodo.parametros]
                        for name in reversed(param_names):
                            if self.param_stack: new_frame[name] = self.param_stack.pop()
                    self.memory_stack.append(new_frame)
                    next_pc = self.labels[f"{func_name}_entry"]
                else:  # Caso: x = y + z or x = y
                    if len(expr_parts) == 1:
                        result = self._get_value(expr_parts[0])
                    else:
                        left = self._get_value(expr_parts[0])
                        op = expr_parts[1]
                        right = self._get_value(expr_parts[2])
                        if op == '+':
                            result = left + right
                        elif op == '-':
                            result = left - right
                        elif op == '*':
                            result = left * right
                        elif op == '/':
                            result = left / right if right != 0 else 0.0
                        elif op == '<':
                            result = left < right
                        elif op == '>':
                            result = left > right
                        elif op == '==':
                            result = left == right
                        else:
                            result = None
                    self._set_value(dest, result)

            elif command == 'goto':
                next_pc = self.labels[parts[1]]

            elif command == 'if_false':
                cond_var, _, label = parts[1:]
                if not self._get_value(cond_var):
                    next_pc = self.labels[label]

            elif command == 'print':
                # Reconstroi o argumento caso ele contenha espaços (para strings)
                arg_str = " ".join(parts[1:])
                value = self._get_value(arg_str)
                if value is not None:
                    print(value, end='')

            elif command == 'println':
                print()

            elif command == 'read':
                try:
                    user_input = input()
                    self._set_value(parts[1], int(user_input))
                except (ValueError, TypeError):
                    self._set_value(parts[1], user_input)

            elif command == 'param':
                self.param_stack.append(self._get_value(parts[1]))

            elif command == 'call':  # Chamada de função VOID
                func_name, _ = parts[1].split(',')
                self.call_stack.append({'pc': next_pc, 'dest': None})
                new_frame = {}
                simbolo_metodo = self.tabela_simbolos.buscar(func_name)
                if simbolo_metodo and simbolo_metodo.parametros:
                    param_names = [p[1] for p in simbolo_metodo.parametros]
                    for name in reversed(param_names):
                        if self.param_stack: new_frame[name] = self.param_stack.pop()
                self.memory_stack.append(new_frame)
                next_pc = self.labels[f"{func_name}_entry"]

            elif command == 'return':
                return_value = self._get_value(" ".join(parts[1:])) if len(parts) > 1 else None
                if not self.call_stack:
                    break

                return_info = self.call_stack.pop()
                next_pc = return_info['pc']
                dest_var = return_info.get('dest')
                self.memory_stack.pop()
                if dest_var and 'return_value_placeholder' in self.current_memory():
                    self._set_value(self.current_memory().pop('return_value_placeholder'), return_value)
                elif dest_var:
                    self._set_value(dest_var, return_value)

            self.pc = next_pc


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Uso: python tac_executor.py <caminho_para_o_arquivo.tac>")
        sys.exit(1)
    tac_file_path = sys.argv[1]
    if not tac_file_path.endswith('.tac'):
        print("Erro: O arquivo de entrada deve ter a extensão .tac")
        sys.exit(1)
    source_file_path = tac_file_path[:-4] + '.jy'
    try:
        input_stream = FileStream(source_file_path, encoding="utf-8")
        lexer = JavythonLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = JavythonParser(stream)
        tree = parser.program()
        analisador = AnalisadorSemantico()
        walker = ParseTreeWalker()
        walker.walk(analisador, tree)
        if analisador.erros:
            print("Erros semânticos encontrados no arquivo fonte. A execução pode falhar.")
        with open(tac_file_path, 'r', encoding='utf-8') as f:
            instructions_from_file = f.readlines()
        print(f"--- Executando '{tac_file_path}' ---")
        executor = TACExecutor(analisador)
        executor.run(instructions_from_file)
        print("\n--- Fim da Execução ---")
    except FileNotFoundError:
        print(f"Erro: Arquivo '{tac_file_path}' ou '{source_file_path}' não encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")