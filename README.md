# Compiladores

Repositório dedicado às práticas da disciplina de **Compiladores** da **Universidade Federal do Piauí (UFPI)**.

## 🛠️ Dependências

* Python 3.x
* [ANTLR4](https://www.antlr.org/) (versão 4.13.x)

## ✅ Instalação do ANTLR para Python

```bash
pip install antlr4-python3-runtime==4.13.0
```

## 🚀 Gerando o Lexer e Parser com ANTLR

1. Baixe o jar do ANTLR: [antlr-4.13.2-complete.jar](https://www.antlr.org/download.html)
2. Execute o seguinte comando no terminal, na pasta onde está o arquivo `.g4`:

```bash
java -jar antlr-4.13.2-complete.jar -Dlanguage=Python3 Hello.g4
```

Esse comando irá gerar os arquivos necessários para executar o analisador léxico e sintático em Python.

