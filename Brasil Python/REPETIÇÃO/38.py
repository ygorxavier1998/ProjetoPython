'''
Um funcionário de uma empresa recebe aumento salarial anualmente: Sabe-se que:
Esse funcionário foi contratado em 1995, com salário inicial de R$ 1.000,00;
Em 1996 recebeu aumento de 1,5% sobre seu salário inicial;
A partir de 1997 (inclusive), os aumentos salariais sempre correspondem ao dobro do percentual do ano anterior.
 Faça um programa que determine o salário atual desse funcionário. Após concluir isto, altere o programa permitindo que o usuário digite o salário inicial do funcionário.
'''
import datetime 

def Salario(Salario,inicio,AnaAtual):
    Aumento = 0.015
    while(inicio != AnaAtual):
        print(round(Salario,3) , (Aumento*100))
        Salario = (Salario+Aumento)
        Aumento = (Aumento*2)
        inicio +=1



def main():
    #ANO ATUAL
    AnoAtual = datetime.date.today()
    AnoAtual = AnoAtual.year
    
    AnoContratacao = int(input("ANO DE CONTRATAÇÃO"))
    Money = int(input("salario"))
    Salario(Money,AnoContratacao, AnoAtual)



if __name__ == '__main__':
    main()
    