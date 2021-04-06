#Faça um programa que imprima na tela
#apenas os números ímpares entre 1 e 50.


def Impar():
    for x in range(50):
        if(x%2 != 0):
            print("{}".format(x))


if __name__ == '__main__':
    Impar()
