#Faça um programa que imprima na tela os números de 1 a 20, um abaixo do outro. 
# Depois modifique o programa para que ele
#mostre os números um ao lado do outro.

def Numero():
    for x in range(1,20):
        print("{}".format(x))

    for x in range(2,20):
        print("{} {}".format((x),(x+1)))

if __name__ == '__main__':
    Numero()