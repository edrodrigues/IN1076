# Função Soma Dígitos. Soma os algarismos de um número de até 3 digitos.

def somaDigitos(n):
    s = 0
    while n:
        s += n % 10
        n //= 10
    return s