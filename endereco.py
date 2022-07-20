#Classe Endereço
class Endereço():
    def __init__ (self, rua, complemento, cidade, cep):
        self.rua = rua
        self.complemento = complemento
        self.cidade = cidade
        self.CEP = cep

    #Imprime Endereço na tela
    def listar_dados(self):
        print("Rua: {} | Complemento: {} | Cidade: {} | CEP: {}".format(self.rua, self.complemento, self.cidade, self.CEP))

    #Atualizar Endereço
    def atualizar_endereço(self, rua, complemento, cidade, cep):
        self.rua = rua
        self.complemento = complemento
        self.cidade = cidade
        self.CEP = cep