listapares = []
def gerar_lista_pares(n, listapares):
    for i in range(n+1):
        if i % 2 == 0:
            print(i)
            listapares.append(i)
        else:
            continue
    return listapares

n = int(input("digite a extensão da lista: "))
gerar_lista_pares(n, listapares)
