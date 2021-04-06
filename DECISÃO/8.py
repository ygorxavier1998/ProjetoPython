#Faça um programa que pergunte o preço de três produtos e informe
#qual produto você deve comprar,
#sabendo que a decisão é sempre pelo mais barato.



def menor(a,b,c):
    Menor_Preco = min(a,b,c)
    return

if __name__ == '__main__':
    a = float(input())
    A_nome = input()
    b = float(input())
    B_nome = input()
    c = float(input())
    C_nome = input()
    print("produto mais pararo a ser comprar",menor(a,b,c))
