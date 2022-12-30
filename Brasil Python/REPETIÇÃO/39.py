#Faça um programa que leia dez conjuntos de dois valores, o primeiro representando o número do aluno e o segundo representando a sua altura em centímetros.
#  Encontre o aluno mais alto e o mais baixo. Mostre o número do aluno mais alto 
#e o número do aluno mais baixo, junto com suas alturas.







def estatistica(tupla):
    print("MAXIMO: ",max(tupla))
    print("MINIMO: ",min(tupla))




def main():
    ancora = 3
    nome = []
    altura = []
    while(ancora >= 0 ):
        NomeEntrada = input("numero: \n")
        AlturaEntrada = float(input("altura: \n"))
        nome.append(NomeEntrada)
        altura.append(AlturaEntrada)
        ancora -=1
    Es = list(zip(nome,altura))
    estatistica(Es)



if __name__ == '__main__':
    main()
