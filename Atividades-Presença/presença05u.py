class Cliente: 

    def __init__(self, nome, cpf, idade, cidade):   
        self.nome = nome
        self.cpf = cpf
        self.idade = idade
        self.cidade = cidade

class ListaClientes: 
    def __init__(self):
        self.cliente = []

    def add(self, Cliente):  
        self.cliente.append(Cliente)

    def mostrarlista(self):
        #print("Lista de Clientes")
        for Cliente in self.cliente: 
            print(f"Nome: {Cliente.nome} * Cpf: {Cliente.cpf} * Idade: {Cliente.idade} anos * Cidade: {Cliente.cidade}")

lista = ListaClientes()

c1 = Cliente("Eliana", "32165498711", 19, "Fortaleza")
c2 = Cliente("Roberta", "78945612353", 24, "Sobral")
c3 = Cliente("Samuel", "45678912302", 22, "Aracati")

lista.add(c1) 
lista.add(c2) 
lista.add(c3) 

lista.mostrarlista()