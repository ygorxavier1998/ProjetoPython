##aça um programa que calcule o valor total investido por um colecionador em sua coleção de CDs e o valor médio
#gasto em cada um deles.
# O usuário deverá informar a quantidade de CDs e o valor para em cada um.

def media(preco,quantidade):
    return preco/quantidade

if __name__ == '__main__':
    Quantidade = int(input("QUANTIDADE DE CD "))
    dic = {
        'c':0
          }
    soma = 0
    for x in range(Quantidade):
        preco = float(input())
        soma += preco
        dic['c'] += 1

    print(media(soma,dic['c']))