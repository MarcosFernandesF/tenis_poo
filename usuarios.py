from endereco import Endereço

class Usuario():
    def __init__(self, id, nome, idade, email):
        self.id = id
        self.nome = nome
        self.idade = idade
        self.email = email
        
    def listar_dados(self):
        print("ID: {} | Nome: {} | Idade: {} | Email: {}".format(self.id, self.nome, self.idade, self.email))

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

    def get_id(self):
        return self.id

class PessoaFisica(Usuario):
    def __init__(self, id, cpf, nome, idade, email, endereço, carrinho):
        super().__init__(id, nome, idade, email)
        self.CPF = cpf
        self.endereço = endereço
        self.carrinho = carrinho

    def listar_dados(self):
        print("ID: {} | Nome: {} | CPF: {} | Idade: {} | Email: {}".format(self.id, self.nome, self.CPF, self.idade, self.email))

    def atualizar_dados(self, cpf, nome, idade, email):
        self.CPF = cpf
        self.nome = nome
        self.idade = idade
        self.email = email

    def get_id(self):
        return self.id

class PessoaJuridica(Usuario):
    def __init__(self, id, cnpj, nome, idade, email, carrinho):
        super().__init__(id, nome, idade, email)
        self.CNPJ = cnpj
        self.carrinho = carrinho

    def listar_dados(self):
        print("ID: {} | Nome: {} | CPF: {} | Idade: {} | Email: {}".format(self.id, self.nome, self.CNPJ, self.idade, self.email))

    def atualizar_dados(self, cnpj, nome, email):
        self.CNPJ = cnpj
        self.nome = nome
        self.email = email

    def get_id(self):
        return self.id
