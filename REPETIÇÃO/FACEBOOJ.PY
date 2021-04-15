'''
def ret(numero):
    Var_str = str(numero)
    peso = 2
    multi = 0 
    for x in Var_str:
        multi += int(x)*peso
        peso +=1
    resulti = multi%7
    print("{}-{}".format(numero,resulti))

if __name__ == '__main__':
    entrada = int(input())
    Tipo_entrada = type(entrada)
    ancora = False
    if(entrada>=1000 and entrada < 3000 and Tipo_entrada==int):
        ret(entrada)
    else:
        print("ENTRADA INCORRETA")
        while(ancora != True):
            print("DIGITE NOVAMENTE O NUMERO")
            entrada = int(input())
            Tipo_entrada = type(entrada)
            if(entrada>=1000 or entrada < 3000 and Tipo_entrada==int):
                ret(entrada)
                ancora = True

'''