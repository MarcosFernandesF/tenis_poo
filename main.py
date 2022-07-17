from usuarios import Usuario, Admin, PessoaFisica, PessoaJuridica
from tenis_carrinho import Tenis, CarrinhoDeCompras

contas = [] #Lista de contas
admin = Admin('admin01', 'Marcos', '20', 'marcos.rff@grad,ufsc.br')


while True:
    print("1. Cadastrar Usuario")
    print("2. Atualizar Dados")
    print("3. Realizar Compra")
    print("4. Menu Admin")
    print("5. Sair")
    op = int(input("Digite um número para executar uma operação: "))


    if op == 1:
        pass

    elif op == 4:
        print("1. Cadastrar Produto")
        print("2. Alterar dados do produto")
        print("3. Excluir Produto")
        print("4. Excluir Usuário")
        print("5. Voltar ao menu principal")