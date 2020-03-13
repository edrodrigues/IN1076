#raizAproximada usando formula da Aula

def raizAproximada(N,r): # N = Numero qualquer ; r = Palpite
    margem = 1
    continuar = True
    while continuar == True:
        r = (r +N/r)/2
        if ((N - margem <= r*r) and (r*r <= N + margem)):
            continuar = False
        else:
            continuar = True
    print(r)

#Teste

print(raizAproximada(100,9))