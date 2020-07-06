"""
Você precisa ajudar um juiz a decidir se um réu pode fazer delação premiada.

O tempo de um juiz é caro e ele vai alocar um estagiário para preencher seu sistema com diversas informações que
o ajudarão a decidir para cada caso se o réu tem direito aos benefícios da delação.

A delação só pode ser feita em casos que apresentam certas propriedades.

O crime que será delatado tem que ser de maior dano à sociedade do que o crime praticado pelo delator.
Os crimes considerados (em ordem de gravidade) serão:
Roubo (menor gravidade)
Tráfico
Homicídio (maior gravidade)

Se o crime do delator for de roubo ou tráfico e o crime delatado for de homicídio, ele tem direito à delação diretamente
Se o crime do delator for de roubo e o crime delatado for também de roubo, ele só tem direito à delação se o valor do roubo delatado for mais de 5 vezes maior que o do roubo do delator
Se o crime do delator for de roubo e o crime delatado for de tráfico, ele só tem direito à delação se o valor da droga traficada for mais de 3 vezes maior que o do roubo do delator
Se o crime do delator for de tráfico e o crime delatado for de tráfico, ele só tem direito à delação se o valor da droga traficada for mais de 5 vezes maior que o do tráfico do delator
No caso do delator ter cometido um homicídio e quiser delatar um homicídio, a delação será concedida
Se a delação foi concedida, você deve imprimir a seguinte mensagem:
"Delação concedida."
Caso contrário:
"Delação rejeitada."
Casos de erro:
Se qualquer um dos crimes for diferente dos especificados (roubo, tráfico ou homicídio), você deve gerar a seguinte mensagem:
"Crime inválido."

"""

def analisarDelacao():
    # Inserindo Valores
    print("Insira o crime cometido pelo indivíduo delator: roubo, tráfico ou homicídio. Escreva com sinal apropriado e em letras minusculas.")
    crimeDelator = input()
    if crimeDelator != "roubo" or "tráfico" or "homicídio":
        print("Crime inválido")
    else:
        crimeDelator != "homicídio"
        print("Insira somente o número inteiro do valor correspondente ao crime.")
        valorCrimeDelator = int(input())
        print("Insira o crime que o delator deseja reportar: roubo, tráfico ou homicídio. Escreva com sinal apropriado e em letras minúsculas.")
        crimeDelatado = input()
        if crimeDelator != "roubo" or "tráfico" or "homicídio":
            print("Crime inválido")
        else:
            if crimeDelatado != "homicídio":
                print("Insira somente o número inteiro do valor correspondente ao crime.")
                valorCrimeDelatado = int(input())
    # Fim da parte de Inserir Valores

    #Veredicto
    def veredicto():
        if (crimeDelator == "roubo") or (crimeDelator == "tráfico") and (crimeDelatado == "homicídio"):
            return print("Delação concedida.")
        elif (crimeDelator == "roubo") and (crimeDelatado == "roubo") and (valorCrimeDelatado > 5* valorCrimeDelator):
            return print("Delação concedida.")
        elif (crimeDelator == "roubo") and (crimeDelatado == "tráfico") and (valorCrimeDelatado > 3* valorCrimeDelator):
            return print("Delação concedida.")
        elif (crimeDelator == "tráfico") and (crimeDelatado == "tráfico") and (valorCrimeDelatado > 5 * valorCrimeDelator):
            return print("Delação concedida.")


        elif (crimeDelator == "homicídio") and (crimeDelatado == "homicídio"):
            return print("Delação concedida.")
        else:
            return print("Delação rejeitada.")

    # Fim da parte de Veredicto

analisarDelacao()