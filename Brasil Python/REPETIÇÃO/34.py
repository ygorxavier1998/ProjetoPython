'''
Os números primos possuem várias aplicações dentro da Computação, por exemplo na Criptografia.
 Um número primo é aquele que é divisível apenas por um e por ele mesmo. Faça um programa
  que peça um número inteiro e determine se ele
 é ou não um número primo.

 '''

def calte(numero):
    resto = (numero)
    mmc = 0
    for x in range(1,100):
        resto = (resto/x)
        if(round(resto)==resto):
            mmc+=1
        elif(round(resto) != resto):
            x+=1
        if(resto==1 or resto==0):
            break
    print("MMC",mmc)
    if(mmc < 2 ):
        print("PRIMO")
    else:
        print("não primo")

if __name__ == '__main__':
    entrada = int(input())
    calte(entrada)
