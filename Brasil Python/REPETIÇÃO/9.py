#Faça um programa que imprima na tela apenas os números ímpares entre 1 e 50.

def Impar():
    for x in range(1,51):
        if(x%2==1):
            print(x)

if __name__ == '__main__':
    Impar()