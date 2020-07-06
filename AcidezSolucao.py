"""
Escreva um programa que leia o valor do índice de acidez (pH) de uma solução e informe se ela é ácida,
básica ou neutra, sendo que o pH deve estar entre 0 e 14. Caso o usuário digite um valor fora dessa faixa,
deve ser mostrada um mensagem de erro.

A solução é ácida quando o pH é menor que 7

A solução é básica quando o pH é maior que 7

Caso contrário a solução é neutra


Formato de entrada

O usuario deve digitar o valor do pH (entre 0.0 e 14.0)

Formato de saída

O programa deve exibir se a solução é ácida, básica ou netra, imprimindo na tela os valores abaixo:

Digite o pH da solucao:

Solucao basica/acida/neutra / Valor do pH deve estar entre 0 e 14

"""

def pHSolucao():
    print("Digite o pH da solucao:")
    PH:float = float(input())
    if PH < 0 or PH > 14:
        return print("Erro. Você deve colocar um valor maior que 0 e menor que 14.0 .")
    elif PH >= 0 or PH < 7:
        return print("Digite o pH da solucao: /n Solucao acida / Valor do pH deve estar entre 0 e 14")
    elif PH > 7 or PH <= 14:
        return print("Digite o pH da solucao: /n  Solucao basica / Valor do pH deve estar entre 0 e 14")
    else:
        PH = 7
        return print("Digite o pH da solucao: /n Solucao basica / Valor do pH deve estar entre 0 e 14")


pHSolucao()