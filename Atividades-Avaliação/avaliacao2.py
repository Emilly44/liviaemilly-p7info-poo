mensagens = [
    "guten morgen meine liebe",
    "bonjour mon amour",
    "buongiorno amore mio",
    "buenos dias cariño",
    "good morning dear",
    "bom dia amor"
]

for mensagens in mensagens:
    nova_mensagem = ""
    maior_len = ""
    i = 0

    while i < len(mensagens.split(" ")):
        nova_mensagem += str(len(mensagens.split(" ")[i])) + "-"
        if len(mensagens.split(" ")[i]) > len(maior_len):
            maior_len = mensagens.split(" ")[i]

        i += 1

    nova_mensagem = nova_mensagem[-len(nova_mensagem):-1]
    print("{:30s} {}".format(nova_mensagem, maior_len))