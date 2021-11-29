class fila:
    def __init__(self):
        self.elementos = list()
    def adiciona(self,novo):
        self.elementos.append(novo) 
    def remove(self):
        del self.elementos[2]
    def exibe(self):
        print(*self.elementos)

clientes = fila()

clientes.adiciona("Manga")
clientes.adiciona("Goiaba")
clientes.adiciona("Maçã")
clientes.adiciona("Uva")

clientes.exibe()
clientes.remove()
clientes.exibe()