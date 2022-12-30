'''
Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa. 
'''
def inverso(list):
    return list[::-1]
def main():
    vet10 = []
    for x in range(1,10,1):
        entrada = int(input("Digite o numero a ser lido {}".format(x)))
        vet10.append(entrada)
    print(inverso(vet10))
    

if __name__ == '__main__':
    main()
    