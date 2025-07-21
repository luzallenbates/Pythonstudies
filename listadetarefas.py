tarefas=[]
def tarefapend():
    inp=""
    while inp != 4:
        print("Ola!  eu sou seu gerenciador de tarefas, oque gostaria de fazer?")
        print("1- Adicionar novas tarefas/2-Ver lista de tarefas/3-Excluir uma tarefa/4-Sair")
        inp = int(input("Digite aqui: "))
        if inp == 1:
            tar = input("Digite sua tarefa: ")
            tarefas.append(tar)
        elif inp == 2:
            if len(tarefas) == 0:
                print("Lista Vazia")
            else:
                for i in range(len(tarefas)):
                    print(f"{i+1} {tarefas[i]}")
        elif inp == 3:
            print("Digite o índice da tarefa a ser excluída: ")
            for j in range(len(tarefas)):
                print(f"{j+1} {tarefas[j]}")
            inp=int(input("índice: "))
            tarefas.pop(inp-1)
        elif inp == 4:
            print("Obrigado por usar o gerenciador de tarefas!")
        else:
            print("Opção inválida")


tarefapend()