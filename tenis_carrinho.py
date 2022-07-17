class Tenis():
    def __init__(self, id, nome, quantidade, valor):
        self.id = id
        self.nome = nome
        self.quantidade = quantidade
        self.valor = valor

    def adicionar_produto(self, quantia):
        self.quantidade += quantia

    #Buscar informações sobre o produto
    def get_id(self):
        return self.id

    def get_nome(self):
        return self.nome

    def get_quantidade(self):
        return self.quantidade

    def get_valor(self):
        return self.valor

class CarrinhoDeCompras():
    def __init__(self):
        self.produtos = []

    def inserir_produto(self, tenis):
        self.produtos.append(tenis)

    def retirar_produto(self, tenis):
        if tenis in self.produtos:
            self.produtos.remove(tenis)
        else:
            print(f"O produto '{tenis.get_nome()}' não está no carrinho de compras!")

    def lista_produtos(self):
        for produto in self.produtos:
            print(f"- {produto.nome} : {produto.valor} R$")

    def soma_total(self):
        soma = 0
        for produto in self.produtos:
            soma += produto.valor

        print(f"Soma total dos preços: {soma}")