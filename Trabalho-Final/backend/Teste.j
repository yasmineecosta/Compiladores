.class public Teste
.super java/lang/Object

; Construtor padrão (obrigatório)
.method public <init>()V
   aload_0
   invokenonvirtual java/lang/Object/<init>()V
   return
.end method

; Método principal
.method public static main([Ljava/lang/String;)V
   .limit stack 2    ; A pilha precisa de espaço para (System.out, valor)
   .limit locals 1   ; Apenas a variavel 'args' (indice 0)

   ; Pega o objeto de saida padrao
   getstatic java/lang/System/out Ljava/io/PrintStream;

   ; Empurra o inteiro 42 para a pilha
   bipush 42

   ; Chama o metodo println que consome um inteiro da pilha
   invokevirtual java/io/PrintStream/println(I)V

   return
.end method