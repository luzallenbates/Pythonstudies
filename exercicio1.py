def parouimpar(n):
    if n % 2 == 0:
        return True
    else:
        return False

n = int(input("Digite um numero inteiro: "))

if parouimpar(n):
    print("O número é par.")
else:
    print("O número é impar.")
    