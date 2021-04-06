'''Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre,
e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:
  Média de Aproveitamento  Conceito
  Entre 9.0 e 10.0        A
  Entre 7.5 e 9.0         B
  #Entre 6.0 e 7.5         C
  Entre 4.0 e 6.0         D
  Entre 4.0 e zero        E

'''
def media(a,b):
    media = (a+b)/2
    if(media >= 9.0 and media ==10.0 ):
        print("ALUNO NOTA A")
        print("APROVADO")
    elif(media >= 7.5 and media <9 ):
        print("ALUNO NOTA B")
        print("APROVADO")
    elif (media >= 6.0 and media < 7.5 ):
        print("ALUNO NOTA C")
        print("APROVADO")
    elif (media >= 4.0 and media < 6):
        print("ALUNO NOTA D")
        print("REPROVADO")
    else:
        print("ALUNO NOTA E")
        print("REPROVADO")

if __name__ == '__main__':
    Nota1 = float(input())
    Nota2 = float(input())

    media(Nota1,Nota2)