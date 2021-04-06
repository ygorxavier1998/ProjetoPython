'''Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda,
que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do
Salário Bruto, mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto
menos os descontos. O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no
mês.
Desconto do IR:
Salário Bruto até 900 (inclusive) - isento
Salário Bruto até 1500 (inclusive) - desconto de 5%
Salário Bruto até 2500 (inclusive) - desconto de 10%
Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o exemplo
abaixo.

#3%  SINDICATO-
#11% FGTS - NÃO E DESCONTADO DO SALRIO;
#10% inss -

#IR
Desconto do IR:
Salário Bruto até 900 (inclusive) - isento
Salário Bruto até 1500 (inclusive) - desconto de 5%
Salário Bruto até 2500 (inclusive) - desconto de 10%
Salário Bruto acima de 2500 - desconto de 20%;
'''

##3%  SINDICATO-
##11% FGTS - NÃO E DESCONTADO DO SALRIO;
##10% inss -

def Salario_Liquido(hora,salario):
    Salario_Bruto = hora*salario
    if(Salario_Bruto <= 900):
        print("SALARIO ISENTO DE DESCONTOS")

    elif(Salario_Bruto >900 and Salario_Bruto <= 1500):
        IR = 0.05*Salario_Bruto
        SINDICATO = Salario_Bruto*0.03
        FGTS = Salario_Bruto*0.11
        INSS = Salario_Bruto*0.10

        print("SALAIO BRUTO:{}".format(Salario_Bruto))
        print("IR 5%: {}".format(IR))
        print("INSS 10%: {}".format(INSS))
        print("SINDICATO 3%:{}".format(SINDICATO))
        print("FGTS:{}".format(FGTS))
        print("TOTAL DE DESCONTO {}".format(IR+INSS))
        print("SALARIO LIQUIDO: {}".format(Salario_Bruto-(IR+INSS)))

    elif (Salario_Bruto > 1500 and Salario_Bruto <= 2500):
        IR = 0.10 * Salario_Bruto
        SINDICATO = Salario_Bruto * 0.03
        FGTS = Salario_Bruto * 0.11
        INSS = Salario_Bruto * 0.10

        print("SALAIO BRUTO:{}".format(Salario_Bruto))
        print("IR 5%: {}".format(IR))
        print("INSS 10%: {}".format(INSS))
        print("SINDICATO 3%:{}".format(SINDICATO))
        print("FGTS:{}".format(FGTS))
        print("TOTAL DE DESCONTO {}".format(IR + INSS))
        print("SALARIO LIQUIDO: {}".format(Salario_Bruto - (IR + INSS)))


    elif (Salario_Bruto > 2500):
        IR = 0.20 * Salario_Bruto
        SINDICATO = Salario_Bruto * 0.03
        FGTS = Salario_Bruto * 0.11
        INSS = Salario_Bruto * 0.10

        print("SALAIO BRUTO:{}".format(Salario_Bruto))
        print("IR 20%: {}".format(IR))
        print("INSS 10%: {}".format(INSS))
        print("SINDICATO 3%:{}".format(SINDICATO))
        print("FGTS:{}".format(FGTS))
        print("TOTAL DE DESCONTO {}".format(IR + INSS))
        print("SALARIO LIQUIDO: {}".format(Salario_Bruto - (IR + INSS)))


if __name__ == '__main__':
    Horas_Trabalhas = int(input())
    Salario_Horas = float(input())
    Salario_Liquido(Horas_Trabalhas,Salario_Horas)