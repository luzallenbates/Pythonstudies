a = input("escreva uma palavra: ")

def palindromo(a):
    return a == a[::-1]

if palindromo(a):
    print("A palavra é um palíndromo.")
else:
    print("A palavra não é um palíndromo.")