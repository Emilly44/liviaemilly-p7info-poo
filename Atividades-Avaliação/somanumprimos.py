print("Digite um número inteiro e positivo: ")
x = int(input())

def primo(p):
      c = 0
      for i in range(1,p+1):
           if p%i==0:
              c = c+1
      if c==2:
          return True

def soma_primos(x):
    soma = 0
    i = 0
    j = 0
    while j < x:
        if primo(i):
            j = j + 1
            soma += i
        i = i + 1
    return soma

print('A soma dos números primos que antecedem o digitado é:', soma_primos(x))
