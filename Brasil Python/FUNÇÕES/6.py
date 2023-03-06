'''
Faça um programa que converta da notação de 24 horas para a notação de 12 horas. 
Por exemplo, o programa deve converter 14:25 em 2:25 P.M. A entrada é dada em dois inteiros.
Deve haver pelo menos duas funções: uma para fazer a conversão e uma para a saída. Registre a 
informação A.M./P.M. como um valor ‘A’ para A.M. e ‘P’ para P.M. Assim, a função para efetuar as
conversões terá um parâmetro formal para registrar se é A.M. ou P.M. Inclua um loop que permita que o 
usuário repita esse cálculo para novos valores de entrada todas as vezes que desejar.

'''


def transforme(horario,denominacao):
    print(horario,denominacao)
    if(denominacao=="PM"):
        
        if(horario=="13"):
            return "01"

        elif(horario=="14"):
            return "02"

        elif(horario=="15"):
            return "03"

        elif(horario=="16"):
            return "04"

        elif(horario=="17"):
            return "05"

        elif(horario=="18"):
            return "06"

        elif(horario=="19"):
                return "07"

        elif(horario=="20"):
                return "08"

        elif(horario=="21"):
                return "09"

        elif(horario=="22"):
                return "10"

        elif(horario=="23"):
                return "11"
            
    if(denominacao=="AM"):
        if(horario=="1"):
            return "13"

        elif(horario=="2"):
            return "14"

        elif(horario=="3"):
            return "15"

        elif(horario=="4"):
            return "16"

        elif(horario=="5"):
            return "17"

        elif(horario=="6"):
            return "18"

        elif(horario=="7"):
            return "19"

        elif(horario=="8"):
            return "20"

        elif(horario=="9"):
            return "21"

        elif(horario=="10"):
            return "22"

        elif(horario=="23"):
            return "11"


horario = input("Qual o horario a ser convertido: ")
tipoHorario = input("AM OU PM: ")


if(tipoHorario=="PM"):
    horarioTransfor = transforme(horario[:2],tipoHorario)
    print("{0}".format(horarioTransfor+horario[2:5]))
    
if(tipoHorario=="AM"):
    horarioTransfor = transforme(horario[:1],tipoHorario)
    print("{0}".format(horarioTransfor+":"+horario[2:5]))