'''
As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e
lhe contraram para desenvolver o programa que calculará os reajustes.
Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte
critério, baseado no salário atual:

salários até R$ 280,00 (incluindo) : aumento de 20%
salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:

o salário antes do reajuste;
o percentual de aumento aplicado;
o valor do aumento;
o novo salário, após o aumento.
'''
def Salario(salario):
        if(salario <= 280):
            print("SALARIO TUAL {}".format(salario))
            print("AUMENTO DE 20%")
            print("AUMENTO DE 20%: {}".format(salario*0.20))
            print("SALARIO + AUMENTO {}".format(salario+(salario * 0.20)))
        elif(salario > 280 and salario <= 700):
            print("SALARIO TUAL {}".format(salario))
            print("AUMENTO DE 15%")
            print("AUMENTO DE 15%: {}".format(salario*0.15))
            print("SALARIO + AUMENTO {}".format(salario + (salario * 0.15)))
        elif(salario > 700 and salario <=1500):
            print("SALARIO TUAL {}".format(salario))
            print("AUMENTO DE 10%")
            print("AUMENTO DE 10%: {}".format(salario*0.10))
            print("SALARIO + AUMENTO {}".format(salario+(salario * 0.10)))
        elif(salario > 1500):
            print("SALARIO TUAL {}".format(salario))
            print("AUMENTO DE 5%%")
            print("AUMENTO DE 5 %: {}".format(salario*0.05))
            print("SALARIO + AUMENTO {}".format(salario + (salario * 0.05)))


if __name__ == '__main__':
    entrada  = float(input())
    Salario(entrada)