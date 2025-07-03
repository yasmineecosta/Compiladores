.class public HelloWorld
.super java/lang/Object

; Construtor padrao
.method public <init>()V
   aload_0
   invokespecial java/lang/Object/<init>()V
   return
.end method

; Metodo principal
.method public static main([Ljava/lang/String;)V
.limit stack 99
   .limit locals 1
   getstatic java/lang/System/out Ljava/io/PrintStream;
   ldc "Hello, World from Javython!"
   invokevirtual java/io/PrintStream/println(Ljava/lang/String;)V
   getstatic java/lang/System/out Ljava/io/PrintStream;
   ldc "Testing numbers: "
   invokevirtual java/io/PrintStream/println(Ljava/lang/String;)V
   getstatic java/lang/System/out Ljava/io/PrintStream;
   bipush 123
   invokevirtual java/io/PrintStream/println(I)V
   return
.end method