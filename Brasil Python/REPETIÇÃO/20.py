#altere o programa de cálculo do fatorial, permitindo ao usuário calcular o fatorial várias vezes e
#limitando o fatorial a números inteiros positivos e menores que 16.

def retorno(numero):
    Multi = 1
    for x in range(numero,1,-1):
        Multi += ((x-1) * Multi)
        print(Multi)



if __name__ == '__main__':
    entrada = int(input())
    while(entrada <= 16):
        retorno(entrada)
        entrada = int(input())
