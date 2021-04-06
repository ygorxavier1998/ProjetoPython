#Faça um Programa que leia três números e mostre-os em ordem decrescente.
def back(decrecente):
    print(sorted(decrecente,reverse=True))

if __name__ == '__main__':
    valor0 = float(input())
    valor1 = float(input())
    valor2 = float(input())
lista =[ ]
lista.insert(0,valor0)
lista.insert(1,valor1)
lista.insert(2,valor2)

back(lista)


