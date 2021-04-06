'''
Faça um Programa para leitura de três notas parciais de um aluno. O programa deve calcular a média 
alcançada por aluno e presentar:

A mensagem "Aprovado", se a média for maior ou igual a 7, com a respectiva média alcançada;
A mensagem "Reprovado", se a média for menor do que 7, com a respectiva média alcançada;
A mensagem "Aprovado com Distinção", se a média for igual a 10.
'''
import math as pedrinho



def Resut_Nota(a,b,c):
    media = float
    media = (a+b+c)/3
    if(media==10):
        print("Aprovado com Distinção")
    elif(media < 7):
        print("REPROVADO")
    elif(media >= 7):
        print("APROVADO")
    else:
        print("notas incoretas")

if __name__ == '__main__':
    nota1 = float(input())
    nota2 = float(input())
    nota3 = float(input())
    Resut_Nota(nota1,nota2,nota3)

