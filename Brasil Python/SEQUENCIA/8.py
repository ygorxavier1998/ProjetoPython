#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
#Calcule e mostre o total do seu salário no referido mês.
def TotalSalario(hora,salario):
    hora = int(hora)
    salario = float(salario)
    return hora*salario

if __name__ == '__main__':
    Salario = float(input("SALARIO POR HORA"))
    Horas = int(input("HORAS TRABALHADAS"))
    print("SALARIO {}".format(TotalSalario(Horas,Salario)))