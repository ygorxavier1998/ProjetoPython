'''Faça um Programa que leia um vetor A com 10 números inteiros,
calcule e mostre a soma dos quadrados dos elementos do vetor. 
'''



def main():
    vet = []
    number = 5
    '''LEITURA DE VETOR DE 10 ELEMENTOS'''
    for x in range(number):
        x = int(input("Digite os numeros {}".format(x)))
        vet.append(x)
    for number in vet:
       number *= (number - 2) + 1
       print(number)

if __name__ == '__main__':
    main()
