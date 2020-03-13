# Função da Gordura Corporal de uma pessoa

def imc(peso, altura):
    return peso / (altura*altura)

def gorduraCorporal(altura, peso, idade, genero): # Genero Masculino = 0 , Genero Feminino = 1
    return 1.294*imc(peso, altura) + 0.2*idade - 11.4 * genero - 0.8

# Testes
GC_Ed = gorduraCorporal(1.81,120,34,0)
print(GC_Ed)

GC_AP = gorduraCorporal(1.62,62,71,1)
print(GC_AP)

imc_AP = imc(62,1.61)
print(imc_AP)