'''Faça um Programa que leia um número e exiba o dia correspondente da semana.
(1-Domingo, 2- Segunda, etc.),
se digitar outro valor deve aparecer valor inválido.
'''

def Funcao_Dia(entrada,Pick):
    for x in entrada.keys():
        if(x==Pick):
            print("DIA DA SEMANA---->",entrada.get(x))
            break
    else:
        print("INVALIDO")

if __name__ == '__main__':
    Dias_Semana = dict
    Dias_Semana = { 1:"DOMINGO",
                   2:"SEGUNDA",
                   3:"TERCA",
                   4:"QUARTA",
                   5:"QUINTA",
                   6:"SEXTA",
                   7:"SABADO"
                }

    Pick =int(input())

    Funcao_Dia(Dias_Semana,Pick)

