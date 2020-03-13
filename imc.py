#Função IMC

def imc(peso, altura):
    return peso / (altura*altura)

#Teste
imcEd = imc(120, 1.81)
print(imcEd)