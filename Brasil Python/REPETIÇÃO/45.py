'''
Desenvolver um programa para verificar a nota do aluno em uma prova com 10 questões, o programa d
eve perguntar ao aluno a resposta de cada questão e ao final comparar com o gabarito da prova e
assim calcular o total de acertos e a nota (atribuir 1 ponto por resposta certa). Após cada aluno 
utilizar o sistema deve ser feita uma pergunta se outro aluno vai utilizar o sistema. Após todos 
os alunos terem respondido informar:
Maior e Menor Acerto;
Total de Alunos que utilizaram o sistema;
A Média das Notas da Turma.
'''


from ast import Str


def main():
    respostas = ["A","B","C","D","E","E","D","C","B","A"]
    alunos = {}
    codigo = 1
    while(True):
        for x in range(1,11):
            alunos[codigo] = 0
            RespostaAluno = input("Resposta Aluno:").upper()
            if(RespostaAluno in respostas):
                alunos[codigo] =+ 1

        saida = input("deseja sair S/N").upper()

        if(saida=="S"):
            break
        elif(saida=="N"):
            codigo =+ 1
            pass


if __name__ == '__main__':
    main()
    