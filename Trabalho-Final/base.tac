label fatorial_entry
t1 = fat > 1
if_false t1 goto L1
t2 = fat - 1
param t2
t3 = call fatorial, 1
t4 = fat * t3
return t4
goto L2
label L1
return 1
label L2
label mostrarMedia_entry
t5 = v1 + v2
t6 = t5 / 2.0
x = t6
print "Resultado: "
print x
println
return
label main_entry
print "Programa Fatorial Digite o valor?"
println
read numero
print "O fatorial e: "
param numero
t7 = call fatorial, 1
print t7
println
print "Programa Media Digite os valores?"
println
read n1
read n2
param n1
param n2
call mostrarMedia, 2
i = 0
label L3
t8 = i < 10
if_false t8 goto L4
print "Teste for."
println
t9 = i + 1
i = t9
goto L3
label L4
return
