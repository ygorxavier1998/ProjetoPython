#Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
#"Telefonou para a vítima?"
#"Esteve no local do crime?"
#"Mora perto da vítima?"
#"Devia para a vítima?"
#"Já trabalhou com a vítima?" O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. 
# Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". 
# Caso contrário, ele será classificado como "Inocente".
# 2 - suspeita
# 3 a 4  - CUMPLICE
#  5 - ASSISSINO 




def main():
    
    perguntas = ["Telefonou para a vítima?","Esteve no local do crime?","Mora perto da vítima?",
                 "Devia para a vítima?","Já trabalhou com a vítima?"
                 ]
    incriminatorio = 0
    for pergunta in perguntas:
        print(pergunta);
        resposta = input("SIM OU NÂO: ").upper()
        if(resposta =="SIM"):
            incriminatorio+=1
        else:
            continue
    if(incriminatorio < 2):
        print("Não suspeita")
    elif(incriminatorio == 2):
        print("suspeita, procure a delegacia")
    elif(incriminatorio >=3 and incriminatorio < 4):
        print(" CUMPLICE!!!! Esta preso chefia")
    elif(incriminatorio >= 4):
        print("Preso Chefia")
if __name__ == '__main__':
    main()