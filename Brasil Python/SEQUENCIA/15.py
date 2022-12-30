'''Faça um Programa que pergunte quanto você ganha por hora e o número
de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês,
sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o
sindicato, faça um programa que nos dê:
salário bruto.
quanto pagou ao INSS.
quanto pagou ao sindicato.
o salário líquido.
'''
def Salario_Liquido(salario):
    IR = salario*(11/100)
    INSS = salario*(8/100)
    Sindicado = salario*(5/100)

    desconto = (IR+INSS+Sindicado)
    return salario - desconto

if __name__ == '__main__':
    salario = float(input("salario:"))
    horas = int(input("horas:"))
    print("SALARIO BRUTO {}:".format(salario*horas))
    print("SALARIO LIQUIDO {}".format(Salario_Liquido(salario*horas)))

