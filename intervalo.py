#Função Intervalo pra ver se um numero x está entre y e z. Caso sim, retorna True. Caso não, retorna False.

def intervalo(x,y,z):
    if x>y and x<z:
        return True
    else:
        return False

#Teste
print(intervalo(15,1,99))