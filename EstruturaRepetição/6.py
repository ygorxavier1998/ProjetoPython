#Faça um programa que imprima na tela os números de 1 a 20,
#um abaixo do outro. Depois modifique o programa para que ele mostre os números um ao lado do outro.


if __name__ == '__main__':
    for x in range(21):
        print(x)
    
    for x in range(20):
        print("{} {}".format(x,(x+1)))