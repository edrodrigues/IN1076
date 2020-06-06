# Trivia StarWars - 5 perguntas

def trivia():
    Pergunta1 = "Em que ano foi lançado o primeiro filme de Star Wars no cinema?"
    RespostaPergunta1 = "1977"

    Pergunta2 = "Qual o nome do mestre Jedi que é verde e pequeno?"
    RespostaPergunta2 = "Yoda"

    Pergunta3 = "Qual o primeiro nome do protagonista da trilogia original de Star Wars?"
    RespostaPergunta3 = "Luke"

    Pergunta4 = "O nome do vilão que se veste de preto e tem uma voz metálica é Darth ..."
    RespostaPergunta4 = "Vader"

    Pergunta5 = "Escreva a letra da opção que NÃO é o nome de um título de filme da saga Star Wars. /n A) Uma nova Esperança /n B) O Retorno do Jedi /n C) Os Jedis Contra Atacam "
    RespostaPergunta5 = "C"

# Funções Fazer Perguntas
    fazerPergunta1(Pergunta1, RespostaPergunta1)
    fazerPergunta2(Pergunta2, RespostaPergunta2)
    fazerPergunta3(Pergunta3, RespostaPergunta3)
    fazerPergunta4(Pergunta4, RespostaPergunta4)
    fazerPergunta5(Pergunta5, RespostaPergunta5)

def fazerPergunta(pergunta, resposta):
    print(pergunta)
    palpite = input()
    score == 0
    if palpite == resposta:
        print ("Parabéns! Você é um(a) Nerd Raiz.")
        score += 1
    else:
        print("Errado. Você é um nerd Nutella.")

# Inicia o Jogo
trivia()