'''
Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a média de cada aluno, ]
imprima o número de alunos com média maior ou igual a 7.0.

'''

def media(dict):
    media = float
    Aluno = dict.keys()
    for x in dict.keys():
        media = (sum(dict[x])/4)
        if(media >= 7.0):
            print(x , media)
        else:
            continue

def main():
    DicNotas= {}
    NomeAluno = str
    for x in range(10):
        NomeAluno = []
        notas = []
        NomeAluno = input("Digte o NOME do aluno\n")
        print(x)
        for x in range(4):
            nota = float(input("Digite A NOTA do aluno\n"))
            notas.append(nota)
        DicNotas[NomeAluno] = notas
    
    print(DicNotas)
    media(DicNotas)
if __name__ == '__main__':
    main()
    