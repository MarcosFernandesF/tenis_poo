from usuarios import Usuario, Admin, PessoaFisica, PessoaJuridica
from tenis_carrinho import Tenis, CarrinhoDeCompras
from endereco import Endereço

endereco = Endereço("Lauro Linhares", "Não sei", "Florianópolis", "88036-000")
admin = Admin(20, 'Marcos', 20, 'marcos.rff@grad,ufsc.br')
usuario_cpf = PessoaFisica(21, '128.991.219-01', 'MarcosCPF', 21, 'marcosrff.2001@gmail.com', endereco)
usuario_cnpj = PessoaJuridica(22, '83.899.526/0001-82', 'MarcosCNPJ', 22, 'marcos.empresa@gmail.com')

lista_usuarios = [] #Lista de usuarios
lista_produtos = [] #Lista de produtos
estoque = {} #Estoque, dicionario
id = 0 # ID do usuário
id_tenis = 0 # ID do tenis

lista_usuarios.append(admin)
lista_usuarios.append(usuario_cpf)
lista_usuarios.append(usuario_cnpj)

while True:
    print("-----------------Menu Principal------------------")
    print("1. Cadastrar Usuario")
    print("2. Atualizar Dados") 
    print("3. Atualizar Endereço") #É preciso listar o endereço em algum momento
    print("4. Realizar Compra") 
    print("5. Menu Admin")
    print("6. Sair")
    op = int(input("Digite um número para executar uma operação: "))
    print()


    if op == 1:
        print("Tela de Cadastro")
        print("1. Pessoa Física")
        print("2. Pessoa Jurídica")
        op = int(input("Digite '1' ou '2' para escolher uma das opções: "))
        print() 
        id += 1
        email = input("Email: ")
        nome = input("Nome: ")
        
        if op == 1:
            idade = int(input("Idade: "))
            cpf = input("CPF: ")
            rua = input("Rua: ")
            complemento = input("Complemento: ")
            cidade = input("Cidade: ")
            cep = input("CEP: ")

            endereço = Endereço(rua, complemento, cidade, cep)
            usuario = PessoaFisica(cpf, id, nome, idade, email, endereço)
            lista_usuarios.append(usuario)

            print("Pessoa Física cadastrada com sucesso!")
            print(f"Seu ID é: {usuario.get_id()}")
            print("")

        elif op == 2:
            cnpj = input("CNPJ")

            usuario = PessoaJuridica(cnpj, id, nome, email)
            lista_usuarios.append(usuario)

            print("Pessoa Jurídica cadastrada com sucesso!")
            print(f"Seu ID é: {usuario.get_id}")
            print("")

    elif op == 2:
        id = int(input("Deseja atualizar os dados de qual conta? Digite o ID: "))
        pessoa = input("Pessoa Física ou Jurídica? [F/J]: ").upper()

        for posicao, dados in enumerate(lista_usuarios):
            if id == dados.get_id():
                email = input("Email: ")
                nome = input("Nome: ")
                idade = int(input("Idade: "))

                if pessoa == 'F':
                    cpf = input("CPF: ")
                    usuario = dados.atualizar_dados(cpf, nome, idade, email)
                    print("Dados atualizados com sucesso!")
                    break
                elif pessoa == 'J':
                    cnpj = input("CNPJ: ")
                    usuario = dados.atualizar_dados(cnpj, nome, idade, email)
                    print("Dados atualizados com sucesso!")
                    break
        else:
            print("A conta não existe!")

    
    elif op == 3:
        id = int(input("Digite o ID da conta que deseja mudar o endereço: "))
        pessoa = input("Pessoa Física ou Jurídica? [F/J]: ").upper()

        for posicao, dados in enumerate(lista_usuarios):
            if id == dados.get_id():
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
            else:
                print("Essa conta não existe!")
                print("")
    
    elif op == 5:
        while True: #Laço para continuar no mesmo menu mesmo após terminar a operação
            print("--------------------Menu ADMIN--------------------")
            print("1. Cadastrar Produto")
            print("2. Alterar dados do produto")
            print("3. Excluir Produto")
            print("4. Excluir Usuário")
            print("5. Voltar ao menu principal")
            op = int(input("Digite um número para executar uma operação: "))
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

            elif op == 2:
                for i in range (len(lista_produtos)):
                    lista_produtos[i].listar_dados()
                
                print("")
                id_produto = int(input("Digite o ID do produto que deseja modificar: "))

                for posicao, dados in enumerate(lista_produtos):
                    if id_produto == dados.get_id():
                        nome_antigo = dados.get_nome()
                        nome = input("Nome do produto: ")
                        quantidade = int(input("Quantidade: "))
                        valor = float(input("Preço: "))

                        estoque[nome_antigo] = quantidade
                        lista_produtos[posicao].atualizar_dados(nome,quantidade,valor)
                        print("Produto alterado com sucesso!")
                        print("")
                    else:
                        print("Esse produto não existe ")

            elif op == 3:
                for i in range (len(lista_produtos)):
                    lista_produtos[i].listar_dados()
                
                print("")

                id_produto = int(input("Digite o ID do produto que deseja excluir: "))
                for posicao, dados in enumerate(lista_produtos):
                    if id_produto == dados.get_id():
                        print(estoque.pop(dados.get_nome(), "Produto não encontrado"))
                        lista_produtos.remove(dados)

                        print("Produto excluído com sucesso!")
                        print("")

            elif op == 4:
                for i in range (len(lista_usuarios)):
                    lista_usuarios[i].listar_dados()
        
                print("")

                id = int(input("Digite o ID do usuario que deseja excluir: "))
                for posicao, dados in enumerate(lista_usuarios):
                    if id == dados.get_id():
                        lista_usuarios.remove(dados)
                        print("Usuário excluído com sucesso!")
                        print("")

            elif op == 5:
                break

            else:
                print("Numero inválido")
                print("")
