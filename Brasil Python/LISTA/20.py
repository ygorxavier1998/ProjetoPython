'''
As Organizações Tabajara resolveram dar um abono aos seus colaboradores em reconhecimento ao bom resultado alcançado durante o ano que passou. Para isto contratou você para desenvolver a aplicação que servirá como uma projeção de quanto será gasto com o pagamento deste abono.

    Após reuniões envolvendo a diretoria executiva, a diretoria financeira e os representantes do sindicato laboral, chegou-se a seguinte forma de cálculo: 

    a.Cada funcionário receberá o equivalente a 20% do seu salário bruto de dezembro; a.O piso do abono será de 100 reais, isto é, aqueles funcionários cujo salário for muito baixo, 
    recebem este valor mínimo; Neste momento, não se deve ter nenhuma preocupação com colaboradores com tempo menor de casa, descontos, impostos ou outras particularidades. Seu programa deverá permitir a digitação do salário de um número indefinido (desconhecido) de salários. Um valor de salário igual a 0 (zero) encerra a digitação. Após a entrada de todos os dados o programa deverá calcular o valor do abono concedido a cada colaborador, de acordo com a regra definida acima. Ao final, o programa deverá apresentar:
    O salário de cada funcionário, juntamente com o valor do abono;
    O número total de funcionário processados;
    O valor total a ser gasto com o pagamento do abono;
    O número de funcionário que receberá o valor mínimo de 100 reais;
    O maior valor pago como abono; A tela abaixo é um exemplo de execução do programa, apenas para fins ilustrativos. Os valores podem mudar a cada execução do programa. 

'''

def calc(listData):
    calcRet = []
    salario = 0
    for item in listData:
        if((item*0.20) <  100):
            calcRet.append(100)
        else:
            salario += item*0.20
            calcRet.append(salario)
            salario = 0
            
    
    return calcRet

if __name__ == '__main__':
    ConjSalario = []
    while(True):
        salario = float(input("Salario: "))
        ConjSalario.append(salario)
        if(salario==0):break
    retList = calc(ConjSalario)
    
    print("Salário ---- abono")
    for salario,abono in zip(ConjSalario,retList):
        print("-------------------------------------")
        print("R$ {} - R$ {}".format(salario,abono))
        print("-------------------------------------")