class Endereço():
    def __init__ (self, rua, complemento, cidade, cep):
        self.rua = rua
        self.complemento = complemento
        self.cidade = cidade
        self.CEP = cep

    def listar_dados(self):
        print("Rua: {} | Complemento: {} | Cidade: {} | CEP: {}".format(self.rua, self.complemento, self.cidade, self.CEP))

    #Atualizar Endereço, função pronta ou sets?
    def atualizar_endereço(self, rua, complemento, cidade, cep):
        self.rua = rua
        self.complemento = complemento
        self.cidade = cidade
        self.CEP = cep

    '''def set_rua(self, rua):
        self.rua = rua

    def set_complemento(self, complemento):
        self.complemento = complemento

    def set_cidade(self, cidade):
        self.cidade = cidade
    
    def set_CEP(self, cep):
        self.CEP = cep'''