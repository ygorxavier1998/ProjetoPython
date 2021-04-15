#Faça um programa que calcule o fatorial de um número
#inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120




def retorno(numero):
    Multi = 1
    for x in range(numero,1,-1):
        Multi += ((x-1) * Multi)
        print(Multi)



if __name__ == '__main__':
    entrada = int(input())
    retorno(entrada)
