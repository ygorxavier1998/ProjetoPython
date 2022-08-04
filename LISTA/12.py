#Foram anotadas as idades e alturas de 30 alunos. 
#Faça um Programa que determine quantos alunos com mais de 13 anos 
#possuem altura inferior à média de altura desses alunos. 


import math as mt
import numpy as py

def media(ListaALunos):
    pass

def  main():
    Alunos = {
                'nome':[],
                'idade':[],
                'altura':[]
            }
    for aluno in range(2):
        nome = input("Nome do aluno:\n")
        idade = int(input("Digite a IDADE do aluno:\n"))
        altura = float(input("Digite a ALTURA do aluno:\n"))
        Alunos['nome'].append(nome)
        Alunos['idade'].append(idade)
        Alunos['altura'].append(altura)
   
    for item in Alunos.items():
        print(item)

if __name__ == '__main__':
    main()
