Controle = 0
Listagem_de_Contatos = []
Listagem_de_Números = []
Listagem_de_E_mail = []
while True:
    def lista(Controle):
        print()
        print("-"*40)
        print("Lista de contatos".center(40))
        print("-"*40)
        print("1- Adicionar um novo contato")
        print("2- Listar contatos")
        print("3- Buscar um contato pelo nome")
        print("4- Editar um contato existente")
        print("5- Remover um contato")
        print("6- Sair do programa")
        print()
        Controle = int(input("O que quer fazer? "))
        return(Controle)
    
    Controle = lista(Controle)
    
    if Controle == 1:
        print()
        print("-"*40)
        print("Adicionar Contato".center(40))
        print("-"*40)
        Nome = input(f"Nome do contato: ")
        Telefone = input(f"Telefone do contato: ")
        E_mail = input(f"E-mail do contato: ")
        if Nome in Listagem_de_Contatos:
            print("Erro! Contato já adicionado!")
        else:
            Listagem_de_Contatos.append(Nome)
            Listagem_de_Números.append(Telefone)
            Listagem_de_E_mail.append(E_mail)
        
    elif Controle == 2:
        print("-"*40)
        print("Listar Contatos".center(40))
        print("-"*40)
        for i in range(len(Listagem_de_Contatos)):
            print(f"{i+1} - {Listagem_de_Contatos[i]} | {Listagem_de_Números[i]} | {Listagem_de_E_mail[i]}")
            
    elif Controle == 3:
        print()
        Pesquisa_Contato = str(input("Diga o nome do contato: "))
        indice = Listagem_de_Contatos.index(Pesquisa_Contato)
        if Pesquisa_Contato in Listagem_de_Contatos:
            print()
            print(f"{Listagem_de_Contatos[indice]} | {Listagem_de_Números[indice]} | {Listagem_de_E_mail[indice]}")
        else:
            print("Contato não encontrado!")
            continue
            
    elif Controle == 4:
        print(Listagem_de_Contatos)
        Editor_de_Contato = str(input("Qual contato deseja editar? "))
        if Editor_de_Contato in Listagem_de_Contatos:
            indice = Listagem_de_Contatos.index(Editor_de_Contato)
            Nome = input(f"Novo nome do contato: ")
            Telefone = input(f"Novo telefone do contato: ")
            E_mail = input(f"Novo e-mail do contato: ")
            Listagem_de_Contatos[indice] = Nome
            Listagem_de_Números[indice] = Telefone
            Listagem_de_E_mail[indice] = E_mail
        else:
            print("Contato não encontrado!")
            continue
    
    elif Controle == 5:
        print(Listagem_de_Contatos)
        Deletor_de_Contato = str(input("Qual contato deseja excluir? "))
        if Deletor_de_Contato in Listagem_de_Contatos:
            indice = Listagem_de_Contatos.index(Deletor_de_Contato)
            Listagem_de_Contatos.pop(indice)
            Listagem_de_Números.pop(indice)
            Listagem_de_E_mail.pop(indice)
            print("Contato excluido!")
        else:
            print("Contato não encontrado!")
            continue
            
    elif Controle == 6:
        print()
        print("Fechando lista...")
        break
    
# Code by Davi Gonçalves Luiz / JAVABEAR16
