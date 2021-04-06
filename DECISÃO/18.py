#Faça um Programa que peça uma data no formato dd/mm/aaaa 
#e determine se a mesma é uma data válida.

def Validacão(Data):
    ancora = 0
    d = Data.split("/")
    dd = int(d[0])
    mm = int(d[1])
    aa = (d[2])

    if(dd<31 and mm < 12 and len(aa)==4):
        return 0
    else:
        return 1

if __name__ == '__main__':  
    try:
        ancora  = 1
        while(ancora != 0):
            print("DIGITE A DATA NO PADRÃO A BAIXO\n")
            print("dd/mm/aaaa")
            data = input()
            if(Validacão(data)==0):
                print("DATA DE ENTRADA CORRETA {}".format(data))
                ancora  = 0
                break
            else:
                print("DATA DE ENTRADA INCORRETA")

    except ValueError:
            print("VOCÊ DIGITOU UMA DATA ERRADA TENTE NOVAMENTE")
            print("DIGITE A DATA NO PADRÃO A BAIXO\n")
            print("dd/mm/aaaa")
            data = input()
            if(Validacão(data)==0):
                print("DATA DE ENTRADA CORRETA {}".format(data))
            else:
                print("DATA DE ENTRADA INCORRETA")
   
        
  