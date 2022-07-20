from re import I


class Tenis():
    def __init__(self, id, nome, quantidade, valor):
        self.id = id
        self.nome = nome
        self.quantidade = quantidade
        self.valor = valor

    def adicionar_produto(self, quantidade):
        self.quantidade += quantidade

    def reduzir_produto(self, quantidade):
        self.quantidade -= quantidade

    def listar_dados(self):
        print("ID: {} | Nome: {} | Quantidade: {} | Valor: {} R$" .format(self.id, self.nome, self.quantidade, self.valor))

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
    

class CarrinhoDeCompras():
    def __init__(self):
        self.produtos = {}

    def inserir_produto(self, tenis, quantidade):
        if tenis.get_nome() not in self.produtos:
            self.produtos[tenis.get_nome()] = 
        else:
            self.produtos[tenis.get_nome()] += quantidade

    def retirar_produto(self, tenis, quantidade):
        if tenis.get_nome() in self.produtos:
            if self.produtos[tenis.get_nome()] > 1:
                self.produtos[tenis.get_nome()] -= quantidade
            else:
                del self.produtos[tenis.get_nome()]
        else:
            print(f"O produto '{tenis.get_nome()}' não está no carrinho de compras!")

    def lista_produtos(self, lista_produtos, usuario):
        retorno = True
        for produto in self.produtos:
            for tenis in lista_produtos:
                if produto == tenis.get_nome():
                    print(f"- {produto} : {tenis.get_valor()} R$ | Quantidade: {self.produtos[produto]}")
                    soma = usuario.carrinho.soma_total(lista_produtos)
                    print(f"- Soma total dos preços = {soma} R$")
                    retorno = False
        return retorno

    def soma_total(self, lista_produtos):
        soma = 0
        for produto in self.produtos:
            for tenis in lista_produtos:
                if produto == tenis.get_nome():
                    quantidade = self.produtos[produto]
                    preço = tenis.get_valor()
                    soma += (preço*quantidade)
        return soma

    def realizar_compra(self, lista_produtos, estoque):
        for produto in self.produtos:
            for tenis in lista_produtos:
                for tenis_est in estoque:
                    if produto == tenis.get_nome() and produto == tenis_est:
                        tenis.reduzir_produto(self.produtos[produto])
                        estoque[tenis_est] -= (self.produtos[produto])
        self.produtos = {}
        print("Compra realizada com sucesso.")
        print("")
