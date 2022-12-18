'''

A ACME Inc., uma empresa de 500 funcionários, está tendo problemas de espaço em disco no seu servidor de arquivos.
Para tentar resolver este problema, o Administrador de Rede precisa saber qual o espaço ocupado pelos usuários, e 
identificar os usuários com maior espaço ocupado. Através de um programa, baixado da Internet, ele conseguiu gerar o 
seguinte arquivo, chamado "usuarios.txt":
'''
from prettytable import PrettyTable
table = PrettyTable()


arquivo = open("23.txt")
linhas  =  arquivo.readlines()
#---------------------------------------------------------#
data = linhas
espacoPessoa = {}
contador = 1

for item in data:
    price = item.split(" ")[-1].replace("\n","")
    espacoPessoa[item.split(" ")[0]] = float(price)
   

totalEspeço  = list(([item for item in espacoPessoa.values()]))
totalEspeço = sum(totalEspeço)
media = (totalEspeço/6)
saida_Str = str(totalEspeço)

table.field_names=["Nr","Usuário","Espeço Utilizado Mb", "% do uso"]
for chave, valo in zip(espacoPessoa.keys(), espacoPessoa.values()):
    table.add_row([contador,chave,valo,((valo/totalEspeço)*100)])
    contador+=1
   
table.add_row(["Espaço total ocupado:",totalEspeço,"MB",""])
table.add_row(["Espaço média ocupado:",media,"MB",""])
table.float_format = '.2'


print(table)


#----------------------------------------------------------------#
teste = open("arquivos.txt", "w")

teste.writelines(saida_Str)

