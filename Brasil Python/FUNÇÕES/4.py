'''
Faça um programa, com uma função que necessite de um argumento. 
A função retorna o valor de caractere ‘P’, se seu argumento for positivo, e ‘N’, 
se seu argumento for zero ou negativo.

'''

def pick(number):
    if(number>0):return 'p'
    else:return 'n'



entrada = int(input())
print(pick(entrada))
    