num =  int(input("Insira um numero inteiro: "))

def tabuada(num):
    for i in range(10):
        print(f"{num} x {i+1} = {num * (i+1)}")

tabuada(num)