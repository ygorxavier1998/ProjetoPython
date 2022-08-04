'''
Faça um Programa que leia um vetor de 5 números inteiros e mostre-os. 

'''
def main():
    vet = []
    for x in range(1,6,1):
        entrada = int(input("DIGITE O NUMERO"))
        vet.append(entrada)
    print("{}".format(vet))

if __name__ == '__main__':
    main()
