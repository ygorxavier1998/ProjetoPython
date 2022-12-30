'''
Faça um programa que receba dois números inteiros
e gere os números inteiros que estão no intervalo compreendido por eles.
'''

def sequencia(primeiro,segundo):
    while(primeiro != segundo):
        print(primeiro)
        primeiro += 1


if __name__ == '__main__':
    primeiro = int(input())
    segundo = int(input())
    sequencia(primeiro,segundo)
