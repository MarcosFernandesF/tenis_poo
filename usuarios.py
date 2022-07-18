from endereço import Endereço

class Usuario():
    def __init__(self, id, nome, idade, email):
        self.id = id
        self.nome = nome
        self.idade = idade
        self.email = email
        
    #Atualização de dados, função pronta ou sets?
    def atualizar_dados(self, nome, idade, email):
        self.nome = nome
        self.idade = idade
        self.email = email

    '''def set_id(self, id):
        self.id = id

    def set_nome(self, nome):
        self.nome = nome    
    
    def set_idade(self, idade):
        self.idade = idade
    
    def set_email(self, email):
        self.email = email'''
         

class Admin(Usuario):
    def __init__(self, id, nome, idade, email):
        super().__init__(id, nome, idade, email)

class PessoaFisica(Usuario):
    def __init__(self, cpf, id, nome, idade, email, endereço):
        super().__init__(id, nome, idade, email)
        self.CPF = cpf
        self.endereço = endereço

    def atualizar_dados(self, cpf, nome, idade, email):
        self.CPF = cpf
        self.nome = nome
        self.idade = idade
        self.email = email

    def get_id(self):
        return self.id

class PessoaJuridica(Usuario):
    def __init__(self, cnpj, id, nome, email):
        super().__init__(id, nome, email)
        self.CNPJ = cnpj

    def atualizar_dados(self, cnpj, nome, email):
        self.CNPJ = cnpj
        self.nome = nome
        self.email = email

    def get_id(self):
        return self.id
