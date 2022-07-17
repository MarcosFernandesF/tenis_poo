class Usuario():
    def __init__(self, id, nome, idade, email):
        self.id = id
        self.nome = nome
        self.idade = idade
        self.email = email
        
    #Atualização de dados, função pronta ou sets?
    def set_id(self, id):
        self.id = id

    def set_nome(self, nome):
        self.nome = nome    
    
    def set_idade(self, idade):
        self.idade = idade
    
    def set_email(self, email):
        self.email = email
         

class Admin(Usuario):
    def __init__(self, id, nome, idade, email):
        super().__init__(id, nome, idade, email)

class PessoaFisica(Usuario):
    def __init__(self, cpf, id, nome, idade, email):
        super().__init__(id, nome, idade, email)
        self.CPF = cpf
        self.endereço = Endereço()

class PessoaJuridica(Usuario):
    def __init__(self, cnpj, id, nome, idade, email):
        super().__init__(id, nome, idade, email)
        self.CNPJ = cnpj
        self.endereço = Endereço()

class Endereço():
    def __init__ (self, rua, complemento, cidade, cep):
        self.rua = rua
        self.complemento = complemento
        self.cidade = cidade
        self.CEP = cep

    #Atualizar Endereço, função pronta ou sets?
    def set_rua(self, rua):
        self.rua = rua

    def set_complemento(self, complemento):
        self.complemento = complemento

    def set_cidade(self, cidade):
        self.cidade = cidade
    
    def set_CEP(self, cep):
        self.CEP = cep