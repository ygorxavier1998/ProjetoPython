'''
Faça um programa que peça dois números, base e expoente, 
calcule e mostre o primeiro número elevado ao segundo número. 
Não utilize a função de potência da linguagem.
'''

def potencia(x,y):
    return x**y

if __name__ == '__main__':
    primeiro =int(input())
    segundo = int(input())
    print(potencia(primeiro,segundo))