'''
Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
"Telefonou para a vítima?"
"Esteve no local do crime?"
"Mora perto da vítima?"
"Devia para a vítima?"

"Já trabalhou com a vítima?" 
O programa deve no final emitir uma classificação sobre a participação da
 pessoa no crime. 
 Se a pessoa responder positivamente a 2 questões ela deve ser 
 classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". 
 Caso contrário, ele será classificado como "Inocente".
'''

def Retorno():

    Disc = 0    
    print("RESPONDA COM S/N OU s/n")

    print("Telefonou para a vítima?")
    Pick = input("?")
    Pick = Pick.upper()

    if(Pick=="S"):
        Disc += 1 
            
    print("Esteve no local do crime")
    Pick = input("?")
    Pick = Pick.upper()

    if(Pick=="S"):
        Disc +=1

    print("Mora perto da vítima?")
    Pick = input("?")
    Pick = Pick.upper()

    if(Pick=="S"):
        Disc +=1

    print("Devia para a vítima")
    Pick = input("?")
    Pick = Pick.upper()
        
    if(Pick=="S"):
        Disc +=1

    print("Já trabalhou com a vítima")
    Pick = input("?")
    Pick = Pick.upper()
        
    if(Pick=="S"):
        Disc +=1

    return Disc



if __name__ == '__main__':
    if(Retorno() == 5):
        print("VOCÊ ESTA PRESO PELA MORTE DE MC POZE")
    elif(Retorno() <= 3 and Retorno() <=4):
        print("DO ASSSINATO DO CÚMPRICE")
    elif(Retorno() == 2):
        print("SUSPEITO DO ASSASINATO DO MC POZE")
    else:
        print("INOCENTE DO ASSASINATO DO MC POZE")   

            
        
