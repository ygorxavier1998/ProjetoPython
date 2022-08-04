'''
Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números. 
'''
def main():
    numeros = []
    numerosmultiplicar = []
    for x in  range(5):
        entrada = int(input())
        numeros.append(entrada)
    soma = print("soma",sum(numeros))
    numerosmultiplicar = lambda x:x
        
if __name__ == '__main__':
    main()