paradas = {
    "subidas": [4,6,7,5,3],
    "descidas": [10,0,9,4,2],
}
in_elevador = []
left_elevador = []
k=0
print("Subiundo")
for i in range(11):
    subiu = False
    desceu = False
    if i == paradas["subidas"][k]:
        subiu = True
        in_elevador.append(paradas["subidas"][k])
        left_elevador.append(paradas["descidas"][k])
        k+= 1
    if i in left_elevador:
        desceu = True
        left_elevador.remove(i)

    if subiu and desceu:
        print(f"Andar {i}: Subiu e desceu")
    elif subiu:
        print(f"andar {i}: Subiu")
    elif desceu:
        print(f"Andar {i}: Desceu")
    else:
        print(f"{i}° Andar")

print("Descendo")

for i in range(10,-1,-1):
    subiu = False
    desceu = False
    if k < len(paradas["subidas"]) and i == paradas["subidas"][k]:
        subiu = True
        in_elevador.append(paradas["subidas"][k])
        left_elevador.append(paradas["descidas"][k])
        k += 1
    if i in left_elevador:
        desceu = True
        left_elevador.remove(i)

    if subiu and desceu:
        print(f"Andar {i}: Subiu e desceu")
    elif subiu:
        print(f"andar {i}: Subiu")
    elif desceu:
        print(f"Andar {i}: Desceu")
    else:
        print(f"{i}° Andar")