#!/usr/bin/env python

#exercicio 1 
print("Alo mundo")


#exercicio 2
x = raw_input("Digite um numero: ")
print("O numero informado foi %s" % (x))

#exercicio 3
x = raw_input("Digite um numero para X: ")
y = raw_input("Digite um numero para Y: ")
print(x+y)

#exercicio 4
jan_fev = raw_input("Digite a nota do seu primeiro bimestre: ")
mar_abr = raw_input("Digite a nota do seu segundo bimestre: ")
mai_jun = raw_input("Digite a nota do seu terceiro bimestre: ")
Jul_ago = raw_input("Digite a nota do seu quarto bimestre: ")
print float(jan_fev + mar_abr + mai_jun + Jul_ago) / 4

#exercicio 5
metro = raw_input("Digite a medida em metros: ")
centimetros = float(metro * 100)
print("A medida em centimetros eh: %s02d" % (centimetros))

