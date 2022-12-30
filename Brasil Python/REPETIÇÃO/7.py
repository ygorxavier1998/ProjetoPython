#Faça um programa que leia 5 números e informe o maior número.

def maior(dado):
    print(max(dado))

if __name__ == '__main__':
    lista = []
    for x in range(5):
        entrada = int(input())
        lista.append(entrada)
    print(lista)
    maior(lista)
