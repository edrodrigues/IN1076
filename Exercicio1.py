"""
Escreva um programa que a partir da média, do número de aulas e faltas do aluno, defina seu resultado na disciplina.

Os resultados possíveis são: APROVADO e REPROVADO. Para ser considerado APROVADO, o aluno precisa se enquadrar

em uma das seguintes situações:

a) Frequência maior ou igual 75% com média maior ou igual a 5;

b) Frequência maior ou igual a 50% caso a média seja maior ou igual a 7.

Caso não se enquadre em pelo menos uma delas, é considerado REPROVADO.


"""

def aprovacao(media:float, aulas:int, faltas:int):
    indiceFaltas = faltas/aulas
    A = (indiceFaltas <= 0.25) and media >= 5.0
    B = (indiceFaltas <= 0.50) and media >= 7.0
    if A or B:
        return print("APROVADO")
    else:
        return print("REPROVADO")

#Testes

aprovacao(5.0,60,15)
aprovacao(4.5, 30, 5)
aprovacao(6.5, 30, 15)
aprovacao(7.0, 60, 28)
