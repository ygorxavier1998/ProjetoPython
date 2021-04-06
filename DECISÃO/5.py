'''Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:
A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
A mensagem "Reprovado", se a média for menor do que sete;
A mensagem "Aprovado com Distinção", se a média for igual a dez.
'''
def Resut_Nota(a,b,):
    media = int
    media = (a+b)/2
    if(media==10):
        print("Aprovado com Distinção")
    elif(media < 7):
        print("REPROVADO")
    elif(media >= 7):
        print("APROVADO")
    else:
        print("notas incoretas")

if __name__ == '__main__':
    nota1 = int(input())
    nota2 = int(input())
    Resut_Nota(nota1,nota2)

