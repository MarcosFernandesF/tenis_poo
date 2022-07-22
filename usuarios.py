#Classe de Usuário
class Usuario():
    def __init__(self, id, nome, idade, email):
        self.id = id
        self.nome = nome
        self.idade = idade
        self.email = email
        
    #Imprime o dado do usuário na tela
    def listar_dados(self):
        print("ID: {} | Nome: {} | Idade: {} | Email: {}".format(self.id, self.nome, self.idade, self.email))

    #Atualização de dados
    def atualizar_dados(self, nome, idade, email):
        self.nome = nome
        self.idade = idade
        self.email = email

#Classe Administradora, herança Usuário
class Admin(Usuario):
    def __init__(self, id, nome, idade, email):
        super().__init__(id, nome, idade, email)

    def get_id(self):
        return self.id

#Classe de Pessoa Física, herança Usuário
class PessoaFisica(Usuario):
    def __init__(self, id, cpf, nome, idade, email, endereço, carrinho):
        super().__init__(id, nome, idade, email)
        self.CPF = cpf
        self.endereço = endereço
        self.carrinho = carrinho

    #Imprime o dado do usuário na tela
    def listar_dados(self):
        print("ID: {} | Nome: {} | CPF: {} | Idade: {} | Email: {}".format(self.id, self.nome, self.CPF, self.idade, self.email))

    #Atualização de dados
    def atualizar_dados(self, cpf, nome, idade, email):
        self.CPF = cpf
        self.nome = nome
        self.idade = idade
        self.email = email

    def get_id(self):
        return self.id

#Classe de Pessoa Jurídica, herança Usuário
class PessoaJuridica(Usuario):
    def __init__(self, id, cnpj, nome, idade, email, carrinho):
        super().__init__(id, nome, idade, email)
        self.CNPJ = cnpj
        self.carrinho = carrinho

    #Imprime o dado do usuário na tela
    def listar_dados(self):
        print("ID: {} | Nome: {} | CNPJ: {} | Email: {}".format(self.id, self.nome, self.CNPJ, self.email))

    #Atualização de dados
    def atualizar_dados(self, cnpj, nome, email):
        self.CNPJ = cnpj
        self.nome = nome
        self.email = email

    def get_id(self):
        return self.id
