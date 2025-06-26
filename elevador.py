p1 = {
    "subida": 4,
    "descida": 10
}
p2 ={
    "subida": 6,
    "descida": 0
}
p3 = {
    "subida": 7,
    "descida":9
}
p4 = {
    "subida": 10,
    "descida":0
}

elevador = [p1, p2, p3, p4]
k = 0
j = 0
holder = 0
holder2 = 0

print("Subindo")
for i in range(11):
    subiu = False
    desceu = False
    
    for j in range(len(elevador)):
        holder = elevador[j]["subida"]
        holder2 = elevador[j]["descida"]
    
        if holder == i:
            subiu = True
        if holder2 == i and holder2 > holder:
            desceu = True
    
    if subiu and desceu:
        if i == 0:
            print(f"térreo: subiu e desceu")
        else:
            print(f"{i}° andar : subiu e desceu")
        elevador[j]["subida"] = -1
        elevador[j]["descida"] = -1
    elif subiu:
        if i == 0:
            print(f"térreo: subiu")
        else:
            print(f"{i}° andar : subiu")
        elevador[j]["subida"] = -1
    elif desceu:
        if i == 0:
            print(f"térreo: desceu")
        else:
            print(f"{i}° andar : desceu")
        elevador[j]["descida"] = -1
    else:
        if i == 0:
            print("térreo")
        else:
            print(f"{i}° andar")

print("\nDescendo")
for i in range(10, -1, -1):
    subiu = False
    desceu = False
    
    for j in range(len(elevador)):
        holder = elevador[j]["subida"]
        holder2 = elevador[j]["descida"]
    
        if holder == i:
            subiu = True
        if holder2 == i and holder2 <= holder:
            desceu = True
    
    if subiu and desceu:
        if i == 0:
            print(f"térreo: subiu e desceu")
            elevador[j]["descida"] = 11
        else:
            print(f"{i} ° andar : subiu e desceu")
            elevador[j]["descida"] = 11
    elif subiu:
        if i == 0:
            print(f"térreo: subiu")
        else:
            print(f"{i}° andar : subiu")
    elif desceu:
        if i == 0:
            print(f"térreo: desceu")
        else:
            print(f"{i}° andar : desceu")
    else:
        if i == 0:
            print("térreo")
        else:
            print(f"{i}° andar")

    
            
        
        
    
            