.class public TesteIf
.super java/lang/Object

.method public <init>()V
   aload_0
   invokespecial java/lang/Object/<init>()V
   return
.end method

.method public static main([Ljava/lang/String;)V
   .limit stack 99
   .limit locals 2
   iconst_5
   iconst_0
   goto L4_comp_end
L3_comp_true:
   iconst_1
L4_comp_end:
   ifeq L1_else
   getstatic java/lang/System/out Ljava/io/PrintStream;
   dup
   ldc "a e maior que 5"
   invokevirtual java/io/PrintStream/print(Ljava/lang/String;)V
   pop
   getstatic java/lang/System/out Ljava/io/PrintStream;
   invokevirtual java/io/PrintStream/println()V
   getstatic java/lang/System/out Ljava/io/PrintStream;
   dup
   ldc "a nao e maior que 5"
   invokevirtual java/io/PrintStream/print(Ljava/lang/String;)V
   pop
   getstatic java/lang/System/out Ljava/io/PrintStream;
   invokevirtual java/io/PrintStream/println()V
   goto L2_endif
L1_else:
   getstatic java/lang/System/out Ljava/io/PrintStream;
   dup
   ldc "a nao e maior que 5"
   invokevirtual java/io/PrintStream/print(Ljava/lang/String;)V
   pop
   getstatic java/lang/System/out Ljava/io/PrintStream;
   invokevirtual java/io/PrintStream/println()V
L2_endif:
   iconst_5
   iconst_0
   goto L8_comp_end
L7_comp_true:
   iconst_1
L8_comp_end:
   ifeq L5_else
   getstatic java/lang/System/out Ljava/io/PrintStream;
   dup
   ldc "a e menor que 5"
   invokevirtual java/io/PrintStream/print(Ljava/lang/String;)V
   pop
   getstatic java/lang/System/out Ljava/io/PrintStream;
   invokevirtual java/io/PrintStream/println()V
L5_else:
   return
.end method