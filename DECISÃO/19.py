'''
Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e
unidades do mesmo.
Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:
326 = 3 centenas, 2 dezenas e 6 unidades
12 = 1 dezena e 2 unidades Testar com:

326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16
'''
def retorno(x):
    tamanho = len(x)
    if(tamanho>3):
        return print("{} MILHAR {} CENTENAS, {} DEZENAS E {} UNIDADES".format(x[0],x[1],x[2],x[3]))
    elif(tamanho==3):
        return print("{} CENTENAS E {} DEZENAS E {} UNIDADES".format(x[0],x[1],x[2]))
    elif(tamanho==2):
        return print("{} DEZENAS E {} UNIDADES".format(x[0],x[1]))
    elif(tamanho==1):
        return print("{} UNIDADES".format(x[0]))

if __name__ == '__main__':
    numero =  input()
    verifica =  int(numero)
    if(verifica<=1000):
        retorno(numero)
    else:
        print("NUMERO MAIOR QUE 1000")