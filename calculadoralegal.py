print("Olá, bem vindo(a) a calculadora de calculos simples")

a = float(input("Insira seu primeiro número: "))
b = float(input("Insira o segundo número: "))
c = input("Insira a operação: ")

if c == "+":
	print(f"Resultado: {a + b}")
elif c == "-":
	print(f"Resultado: {a - b}")
elif c == "*":
	print(f"Resultado: {a * b}")
elif c == "/":
	if b != 0:
		print(f"Resultado: {a / b}")
	else:
		print("Erro: Divisão por zero não é permitida.")
else:
	print("Operação inválida.")