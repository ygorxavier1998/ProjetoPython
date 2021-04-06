'''João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho
. Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo
(50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente.
João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso. Gravar na variável excesso a quantidade
de quilos além do limite e na variável multa o valor da multa que João deverá pagar.
Imprima os dados do programa com as mensagens adequadas.
'''


def Valor(peso):
    if(peso > 50):
        Limite = 50
        Excesso = peso - Limite
        multa = Excesso * 4.0

        print("O LIMITE {}".format(Limite))
        print("O EXCESSO {}".format(Excesso))
        print("VALOR A PAGAR {}".format(multa))
    else:
        print("PESO A BAIXO DA REGULAMENTAÇÃ0 PREVIA 50 km")

if __name__ == '__main__':
    peso = float(input())
    Valor(peso)


