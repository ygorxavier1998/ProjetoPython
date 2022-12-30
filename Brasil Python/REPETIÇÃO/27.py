#Faça um programa que calcule o número médio de alunos por turma. Para isto,
# peça a quantidade de turmas e a quantidade de alunos para cada turma.
#As turmas não podem ter mais de 40 alunos.

def Media(aluno,sala):
    x = aluno
    y = sala
    return x/y


if __name__ == '__main__':
    Quan_Aluno = int(input("QUANTIDADE DE ALUNO"))
    Quan_Turma =  int(input("QUANTIDADE DE TURMA"))
    if(Quan_Turma <= 40):
        print(Media(Quan_Aluno,Quan_Turma))
        
    elif(Quan_Turma > 40):
        while(Quan_Turma > 40): 
            print("ENTRADA NÃO PERMITIDA")
            Quan_Aluno = int(input("QUANTIDADE DE ALUNO"))
            Quan_Turma =  int(input("QUANTIDADE DE TURMA"))
        print(Media(Quan_Aluno,Quan_Turma))
        