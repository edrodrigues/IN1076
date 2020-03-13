#Função pequenar verifica se num > 1000 . Caso sim, divide por 2. Caso não, devolve num.

def pequenar(num):
    if num > 1000:
        return num/2
    else:
        return num

#Teste
print(pequenar(1500))