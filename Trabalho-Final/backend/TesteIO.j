.class public TesteIO
.super java/lang/Object

.method public <init>()V
   aload_0
   invokespecial java/lang/Object/<init>()V
   return
.end method

.method public static main([Ljava/lang/String;)V
   .limit stack 99
   .limit locals 4
   getstatic java/lang/System/out Ljava/io/PrintStream;
   dup
   ldc "Por favor, digite o seu nome:"
   invokevirtual java/io/PrintStream/print(Ljava/lang/String;)V
   pop
   getstatic java/lang/System/out Ljava/io/PrintStream;
   invokevirtual java/io/PrintStream/println()V
   getstatic java/lang/System/out Ljava/io/PrintStream;
   dup
   ldc "Agora, digite a sua idade:"
   invokevirtual java/io/PrintStream/print(Ljava/lang/String;)V
   pop
   getstatic java/lang/System/out Ljava/io/PrintStream;
   invokevirtual java/io/PrintStream/println()V
   getstatic java/lang/System/out Ljava/io/PrintStream;
   dup
   ldc "Ola, "
   invokevirtual java/io/PrintStream/print(Ljava/lang/String;)V
   dup
   invokevirtual java/io/PrintStream/print(Lindefinido;)V
   dup
   ldc "! Se voce tem "
   invokevirtual java/io/PrintStream/print(Ljava/lang/String;)V
   dup
   invokevirtual java/io/PrintStream/print(Lindefinido;)V
   dup
   ldc " anos, voce nasceu em "
   invokevirtual java/io/PrintStream/print(Ljava/lang/String;)V
   dup
   invokevirtual java/io/PrintStream/print(Lindefinido;)V
   dup
   ldc "."
   invokevirtual java/io/PrintStream/print(Ljava/lang/String;)V
   pop
   getstatic java/lang/System/out Ljava/io/PrintStream;
   invokevirtual java/io/PrintStream/println()V
   return
.end method