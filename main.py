from usuarios import Usuario, Admin, PessoaFisica, PessoaJuridica
from tenis_carrinho import Tenis, CarrinhoDeCompras
from endereço import Endereço

admin = Admin('#01', 'Marcos', '20', 'marcos.rff@grad,ufsc.br')
usuario_cpf = PessoaFisica('#02', 'MarcosCPF', '21', 'marcosrff.2001@gmail.com')
usuario_cnpj = PessoaJuridica('#03', 'MarcosCNPJ', 'marcos.empresa@gmail.com')

lista_usuarios = [] #Lista de usuarios
lista_produtos = [] #Lista de produtos
estoque = {} #Estoque, dicionario
id = 0 # ID do usuário
id_tenis = 0 # ID do tenis

while True:

    print("1. Cadastrar Usuario")
    print("2. Atualizar Dados") #Descobrir como diferenciar pessoa fisica de juridica através da classe
    print("3. Atualizar Endereço") #Descobrir como diferenciar pessoa fisica de juridica através da classe
    print("4. Realizar Compra") 
    print("5. Menu Admin") #Op == 3 ERRO
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
        for posicao,dados in enumerate(lista_usuarios):
            if id == dados.get_id():
                pass
                #Descobrir como diferenciar pessoa fisica de juridica através da classe
            else:
                print("Essa conta não existe!")
                print("")
    
    elif op == 3:
        id = int(input("Digite o ID da conta que deseja mudar o endereço: "))
        for posicao, dados in enumerate(lista_usuarios):
            if id == dados.get_id():
                pass
                #Descobrir como diferenciar pessoa fisica de juridica através da classe
            else:
                print("Essa conta não existe!")
                print("")
    
    elif op == 5:
        print("Menu ADMIN")
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
                    lista_produtos[posicao].remove(dados) #Função errada, erro compilação
                    print("Produto excluído com sucesso!")
                    print("")

