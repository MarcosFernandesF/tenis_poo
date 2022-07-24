from usuarios import  Admin, PessoaFisica, PessoaJuridica
from tenis_carrinho import Tenis, CarrinhoDeCompras
from endereco import Endereço

#Usuários e produto pré-definido para facilitar o teste do programa
endereco = Endereço("Lauro Linhares", "Não sei", "Florianópolis", "88036-000") #Endereço pessoa física
carrinho1 = CarrinhoDeCompras() #Fisico
carrinho2 = CarrinhoDeCompras() #Juridico
admin = Admin(20, 'Marcos', 20, 'marcos.rff@grad,ufsc.br') 
usuario_cpf = PessoaFisica(21, '128.303.529-01', 'MarcosCPF', 21, 'marcosrff.2001@gmail.com', endereco, carrinho1)
usuario_cnpj = PessoaJuridica(22, '83.899.526/0001-82', 'MarcosCNPJ', 22, 'marcos.empresa@gmail.com', carrinho2)
produto_exemplo = Tenis(23, 'Nike Air Max', 20, 500.0)


lista_usuarios = [] #Lista de usuarios
lista_produtos = [] #Lista de produtos
estoque = {} #Estoque, dicionario
id_usuario = 0 # ID do usuário
id_tenis = 0 # ID do tenis

#Colocando produto exemplo no estoque
estoque['Nike Air Max'] = 20

#Colocando os usuários e produto nas listas de objeto
lista_usuarios.append(admin)
lista_usuarios.append(usuario_cpf)
lista_usuarios.append(usuario_cnpj)
lista_produtos.append(produto_exemplo)

while True:
    print(" ----------------Menu Principal------------------ ")
    print("| 1. Cadastrar Usuario                           |")
    print("| 2. Atualizar Dados                             |") 
    print("| 3. Atualizar Endereço                          |")
    print("| 4. Comprar Produto                             |") 
    print("| 5. Menu Admin                                  |")
    print("| 6. Sair                                        |")
    op = int(input("| Digite um número para executar uma operação: "))
    print()


    if op == 1:
        print(" -----------------Tela de Cadastro--------------- ")
        print("1. Pessoa Física")
        print("2. Pessoa Jurídica")
        op = int(input("Digite '1' ou '2' para escolher uma das opções: "))
        print() 
        id_usuario += 1
        email = input("Email: ")
        nome = input("Nome: ")
        
        if op == 1:
            idade = int(input("Idade: "))
            cpf = input("CPF: ")
            rua = input("Rua: ")
            complemento = input("Complemento: ")
            cidade = input("Cidade: ")
            cep = input("CEP: ")
            print("")

            endereço = Endereço(rua, complemento, cidade, cep)
            carrinho = CarrinhoDeCompras()
            usuario = PessoaFisica(id_usuario, cpf, nome, idade, email , endereço, carrinho)
            lista_usuarios.append(usuario)

            print("Pessoa Física cadastrada com sucesso!")
            print(f"Seu ID é: {usuario.get_id()}")
            print("")

        elif op == 2:
            cnpj = input("CNPJ: ")
            idade = 0
            print("")

            carrinho = CarrinhoDeCompras()
            usuario = PessoaJuridica(id_usuario, cnpj, nome, idade, email, carrinho)
            lista_usuarios.append(usuario)

            print("Pessoa Jurídica cadastrada com sucesso!")
            print(f"Seu ID é: {usuario.get_id()}")
            print("")

    elif op == 2:
        id = int(input("Deseja atualizar os dados de qual conta? Digite o ID: "))
        pessoa = input("Pessoa Física ou Jurídica? [F/J]: ").upper()
        print("")

        for posicao, dados in enumerate(lista_usuarios):
            if id == dados.get_id():
                email = input("Email: ")
                nome = input("Nome: ")

                if pessoa == 'F':
                    idade = int(input("Idade: "))
                    cpf = input("CPF: ")
                    print("")

                    usuario = dados.atualizar_dados(cpf, nome, idade, email)
                    print("Dados atualizados com sucesso!")
                    print("")
                    break
                elif pessoa == 'J':
                    cnpj = input("CNPJ: ")
                    print("")

                    usuario = dados.atualizar_dados(cnpj, nome, email)
                    print("Dados atualizados com sucesso!")
                    print("")
                    break
        else:
            print("A conta não existe!")

    
    elif op == 3:
        id = int(input("Digite o ID da conta que deseja mudar o endereço: "))
        pessoa = input("Pessoa Física ou Jurídica? [F/J]: ").upper()
        print("")

        for posicao, dados in enumerate(lista_usuarios):
            if id == dados.get_id():
                print("Endereço Atual da Conta: ")
                dados.endereço.listar_dados()
                print("")

                op = input("Ainda deseja atualizar o endereço? [S/N]: ").upper()
                print("")

                if op == 'S':
                    if pessoa == 'F':
                        rua = input("Rua: ")
                        complemento = input("Complemento: ")
                        cidade = input("Cidade: ")
                        cep = input("CEP: ")

                        endereço = dados.endereço.atualizar_endereço(rua, complemento, cidade, cep)
                        print("Endereço atualizado com sucesso!")
                        print("")
                        break
                    elif pessoa == 'J':
                        print("Apenas pessoas físicas possuem endereço ")
                        print("")
                        break
                elif op == 'N':
                    break
                else:
                    print("Resposta inválida.")
                    print("")
        else:
            print("Essa conta não existe!")
            print("")
    
    elif op == 4:
        id = int(input("Digite o ID da conta que deseja fazer as compras: "))
        print("")

        for posicao, usuario in enumerate(lista_usuarios):
            if id == usuario.get_id():
                while True:
                    print(" ----------------Menu de Compra------------------ ")
                    print("| 1. Mostrar Estoque                             |")
                    print("| 2. Adicionar no carrinho                       |")
                    print("| 3. Retirar do carrinho                         |")
                    print("| 4. Mostrar carrinho de compras                 |")
                    print("| 5. Efetuar Compra                              |")
                    print("| 6. Voltar ao menu principal                    |")
                    op = int(input("| Digite um número para executar uma operação: "))
                    print("")

                    if op == 1:
                        print("------------------Estoque------------------")
                        for produto in estoque:
                            for tenis in lista_produtos:
                                if produto == tenis.get_nome():
                                    print(f"Produto: {produto} | Preço: {tenis.get_valor()} R$ | Quantidade: {estoque[produto]}")
                        print("")

                    elif op == 2:
                        print("------------------Estoque------------------")
                        for produto in estoque:
                            for tenis in lista_produtos:
                                if produto == tenis.get_nome():
                                    print(f"ID: {tenis.get_id()} | Produto: {produto} | Preço: {tenis.get_valor()} R$ | Quantidade: {estoque[produto]}")
                        print("")
                        while True:
                            id_produto = int(input("Digite o ID do produto que deseja comprar, caso contrário, digite '0' para sair da compra: "))
                            print("")
                            if id_produto == 0:
                                break
                            else:
                                for tenis in lista_produtos:
                                    if id_produto == tenis.get_id():
                                        quantidade = int(input(f"Digite a quantidade de '{tenis.get_nome()}' que deseja mover para o carrinho: "))
                                        usuario.carrinho.inserir_produto(tenis, quantidade)


                    elif op == 3:
                        print("------------------Carrinho de Compras------------------")
                        usuario.carrinho.lista_produtos(lista_produtos, usuario)

                        while True:
                            id_produto = int(input("Digite o ID do produto que deseja retirar do carrinho, caso contrário, digite '0' para sair da compra: "))
                            print("")
                            if id_produto == 0:
                                break
                            else:
                                for tenis in lista_produtos:
                                    if id_produto == tenis.get_id():
                                        quantidade = int(input(f"Digite a quantidade de '{tenis.get_nome()}' que deseja retirar do carrinho: "))
                                        usuario.carrinho.retirar_produto(tenis, quantidade)

                    elif op == 4:
                        print("------------------Carrinho de Compras------------------")
                        usuario.carrinho.lista_produtos(lista_produtos, usuario)
                        
                    elif op == 5:
                        while True:
                            usuario.carrinho.lista_produtos(lista_produtos, usuario)
                            op = input("Deseja efetuar a compra dos seguintes itens? [S/N]").upper()
                            print("")

                            if op == 'S':
                                usuario.carrinho.realizar_compra(lista_produtos, estoque)
                                break
                            elif op == 'N':
                                break
                            else:
                                print("Dígito inválido")
                                print("")

                    elif op == 6:
                        break
        else:
            print("Essa conta não existe!")
            print("")
            
    elif op == 5:
        while True: #Laço para continuar no mesmo menu mesmo após terminar a operação
            print(" -------------------Menu ADMIN------------------- ")
            print("| 1. Cadastrar Produto                           |")
            print("| 2. Alterar dados do produto                    |")
            print("| 3. Excluir Produto                             |")
            print("| 4. Excluir Usuário                             |")
            print("| 5. Voltar ao menu principal                    |")
            op = int(input("| Digite um número para executar uma operação: "))
            print("")

            if op == 1:
                id_tenis += 1
                nome = input("Nome do produto: ")
                quantidade = int(input("Quantidade: "))
                valor = float(input("Preço: "))
                print("")
                
                produto = Tenis(id_tenis, nome, quantidade, valor)
                lista_produtos.append(produto)

                if nome not in estoque:
                    estoque[nome] = quantidade
                else:
                    print("Esse produto ja existe no estoque.")
                    print("")

            elif op == 2:
                for i in range (len(lista_produtos)):
                    lista_produtos[i].listar_dados()
                
                print("")
                id_produto = int(input("Digite o ID do produto que deseja modificar: "))
                print("")

                for posicao, dados in enumerate(lista_produtos):
                    if id_produto == dados.get_id():
                        nome_antigo = dados.get_nome()
                        nome = input("Nome do produto: ")
                        quantidade = int(input("Quantidade: "))
                        valor = float(input("Preço: "))
                        
                        estoque[nome] = quantidade
                        del estoque[nome_antigo]
                        lista_produtos[posicao].atualizar_dados(nome,quantidade,valor)
                        print("Produto alterado com sucesso!")
                        print("")
                        break
                else:
                    print("Esse produto não existe ")
                    print("")

            elif op == 3:
                for i in range (len(lista_produtos)):
                    lista_produtos[i].listar_dados()
                
                print("")

                id_produto = int(input("Digite o ID do produto que deseja excluir: "))
                print("")
                for posicao, dados in enumerate(lista_produtos):
                    if id_produto == dados.get_id():
                        estoque.pop(dados.get_nome(), "Produto não encontrado")
                        lista_produtos.remove(dados)

                        print("Produto excluído com sucesso!")
                        print("")
                        break
                else:
                    print("Produto não encontrado!")
                    print("")

            elif op == 4:
                for i in range (len(lista_usuarios)):
                    lista_usuarios[i].listar_dados()
        
                print("")

                id = int(input("Digite o ID do usuario que deseja excluir: "))
                print("")

                for posicao, dados in enumerate(lista_usuarios):
                    if id == dados.get_id():
                        lista_usuarios.remove(dados)
                        print("Usuário excluído com sucesso!")
                        print("")
                        break
                else:
                    print("Usuário não encontrado!")
                    print("")

            elif op == 5:
                break

            else:
                print("Operação inválida")
                print("")

    elif op == 6:
        break

    else:
        print("Operação Inválida")
