#Classe do Produto Tenis
class Tenis():
    def __init__(self, id, nome, quantidade, valor):
        self.id = id
        self.nome = nome
        self.quantidade = quantidade
        self.valor = valor

    #Reduz quantidade de produto na classe
    def reduzir_produto(self, quantidade):
        self.quantidade -= quantidade

    #Imprime os dados do produto na tela
    def listar_dados(self):
        print("ID: {} | Nome: {} | Quantidade: {} | Valor: {} R$" .format(self.id, self.nome, self.quantidade, self.valor))

    #Atualiza os dados
    def atualizar_dados(self, nome, quantidade, valor):
        self.nome = nome
        self.quantidade = quantidade
        self.valor = valor
        
    def get_id(self):
        return self.id

    def get_nome(self):
        return self.nome

    def get_valor(self):
        return self.valor

    def get_quantidade(self):
        return self.quantidade
    
#Carrinho de compras
class CarrinhoDeCompras():
    def __init__(self):
        self.produtos = {}

    #Insere uma quantidade produtos no carrinho
    def inserir_produto(self, tenis, quantidade):
        if tenis.get_nome() not in self.produtos:
            self.produtos[tenis.get_nome()] = quantidade
        else:
            self.produtos[tenis.get_nome()] += quantidade

    #Retira uma quantidade de produtos no carrinho
    def retirar_produto(self, tenis, quantidade):
        if tenis.get_nome() in self.produtos:
            if (self.produtos[tenis.get_nome()] - quantidade) < 1:
                del self.produtos[tenis.get_nome()]
            else:
                self.produtos[tenis.get_nome()] -= quantidade
        else:
            print(f"O produto '{tenis.get_nome()}' não está no carrinho de compras!")

    #Imprime os produtos no carrinho de compras
    def listar_produtos(self, lista_produtos, usuario):
        if len(self.produtos) == 0:
            print("Não ha nada no carrinho de compras!")
            print("")
        else:
            for produto in self.produtos:
                for tenis in lista_produtos:
                    if produto == tenis.get_nome():
                        print(f"ID: {tenis.get_id()} | {produto} : {tenis.get_valor()} R$ | Quantidade: {self.produtos[produto]}")
                        soma = usuario.carrinho.soma_total(lista_produtos)
            print(f"Soma total dos preços = {soma} R$")
            print("")

    #Faz a soma do carrinho
    def soma_total(self, lista_produtos):
        soma = 0
        for produto in self.produtos:
            for tenis in lista_produtos:
                if produto == tenis.get_nome():
                    quantidade = self.produtos[produto]
                    preço = tenis.get_valor()
                    soma += (preço*quantidade)
        return soma

    #Realiza a compra, da baixa no estoque
    def realizar_compra(self, lista_produtos, estoque):
        flag = 0
        for produto in self.produtos:
            for tenis in lista_produtos:
                for tenis_est in estoque:
                    if produto == tenis.get_nome() and produto == tenis_est:
                        if self.produtos[produto] > estoque[tenis_est]:
                            print("Quantidade não existente no estoque! ")
                            print("Você deve retirar produto do seu carrinho!")
                            print("")
                        else:
                            flag = 1
                            tenis.reduzir_produto(self.produtos[produto])
                            estoque[tenis_est] -= (self.produtos[produto])
        if flag == 1:
            self.produtos = {}
            print("Compra realizada com sucesso.")
            print("")
