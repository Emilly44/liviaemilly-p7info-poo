class Pilha:
    def __init__(self):
        self.pilha = list()
    
    def inserir(self, elemento):
        self.pilha.append(elemento)
    
    def retirar(self):
        self.pilha.pop()
    
    def mostrarpilha(self):
        for x in self.pilha:
            print(x)

PILHA = Pilha()
PILHA.inserir(19022020)
PILHA.inserir(True)
PILHA.inserir("feijão")
PILHA.inserir("arroz")
PILHA.inserir("batata")
PILHA.retirar()
PILHA.mostrarpilha()
