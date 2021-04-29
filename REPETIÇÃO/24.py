#Faça um programa que calcule o mostre a média aritmética de N notas.

def nota(dados):
    tamanho = len(dados)
    soma = sum(dados)
    return soma/tamanho


if __name__ == '__main__':
    print("PROGRAMA DE NOTAS")
    Quanti_Notas = int(input("QUANTAS NOTAS A SER COMPUTADAS"))
    #
    lista = []
    verade = True
    entrada  = 0
    while(Quanti_Notas != 0):
        nota1 = float(input("\n"))
        lista.append(nota1)
        Quanti_Notas -= 1
    print("MEDIA NOTA",round(nota(lista)))

