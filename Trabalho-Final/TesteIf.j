.class public TesteIf
.super java/lang/Object

; Construtor padrao (obrigatorio)
.method public <init>()V
   aload_0
   invokespecial java/lang/Object/<init>()V
   return
.end method

; Metodo principal
.method public static main([Ljava/lang/String;)V
   .limit stack 99
   .limit locals 1
   iconst_5
   if_icmple L1_else
   getstatic java/lang/System/out Ljava/io/PrintStream;
   ldc "a e maior que 5"
   invokevirtual java/io/PrintStream/println(Ljava/lang/String;)V
   goto L2_endif
L1_else:
   getstatic java/lang/System/out Ljava/io/PrintStream;
   ldc "a nao e maior que 5"
   invokevirtual java/io/PrintStream/println(Ljava/lang/String;)V
L2_endif:
   iconst_5
   if_icmpge L3_else
   getstatic java/lang/System/out Ljava/io/PrintStream;
   ldc "a e menor que 5"
   invokevirtual java/io/PrintStream/println(Ljava/lang/String;)V
L3_else:
   return
.end method