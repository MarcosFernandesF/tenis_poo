from usuarios import Usuario, Admin, PessoaFisica, PessoaJuridica, Endereço
from tenis_carrinho import Tenis, CarrinhoDeCompras

lista_usuarios = [] #Lista de usuarios
admin = Admin('admin01', 'Marcos', '20', 'marcos.rff@grad,ufsc.br')
estoque = {} #Estoque, dicionario

while True:
    id = 0
    print("1. Cadastrar Usuario")
    print("2. Atualizar Dados")
    print("3. Atualizar Endereço")
    print("3. Realizar Compra")
    print("4. Menu Admin")
    print("5. Sair")
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
    print()
    elif op == 4:
        print("1. Cadastrar Produto")
        print("2. Alterar dados do produto")
        print("3. Excluir Produto")
        print("4. Excluir Usuário")
        print("5. Voltar ao menu principal")