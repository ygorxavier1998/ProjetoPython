'''Faça um programa que mostre todos os primos entre 1 e N sendo N um 
número inteiro fornecido pelo usuário. O programa deverá mostrar também o número de +
divisões que ele executou para encontrar os números primos. Serão avaliados o funcionamento,
o estilo e o número de testes (divisões) executados.
'''

def primos(numero):
    mmc = 0
    saida = True
    divisor = 2
    Quanti_Divi = 0

    for x in range(2,numero):
        resto = x
        saida = True
        for y in range(2,100):
            resto = resto/divisor
            if(round(resto)==resto): # SE A DIVISÃO FOR INTERIRA O NUMERO X E IGUAL A O MMC
                mmc+=1
                divisor = 2
                Quanti_Divi += 1
            elif(round(resto) != resto):
                divisor += 1
                resto = x
            if(round(resto)==1 or round(resto)==0):
                #print(x, mmc)
                if(mmc < 2):
                    print("NUMERO PRIMO {} NUMERO DE DIVISÕES REALIZADAS {} ".format(x,Quanti_Divi))
                    mmc = 0
                    x += 1
                    break
                else:
                    mmc = 0
                    x+= 1
                    break



if __name__ == '__main__':
    entrada = int(input())
    primos(entrada)
