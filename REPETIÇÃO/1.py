#Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o 
#valor seja inválido e continue pedindo até que o usuário informe um valor válido.


def NotaRetorno(dado):
    x = dado
    if(x >= 0 and x <=10):
        return True
    else:
        return False



if __name__ == '__main__':
    entrada = int(input())
    if(NotaRetorno(entrada)==True):
       print("nota aceita")
    elif(NotaRetorno(entrada)==False):
        while(NotaRetorno(entrada)==False):
            print("valor invalido")
            entrada = int(input())
            NotaRetorno(entrada)
        print("valor {}".format(entrada))