#Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120


def retorno(entrada):
    multi = 0
    termi = 1
    for x in range(entrada,1,-1):
        if termi == 1:
            multi = x
            termi -=1  # ANCORA PARA O PRIMEIRA DODAD
        else: 
           multi =  multi*x
           print(multi)
        


if __name__ == '__main__':
    entrada = int(input())
    retorno(entrada)