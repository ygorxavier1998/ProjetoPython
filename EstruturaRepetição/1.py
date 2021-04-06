#Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja 
#inválido e continue pedindo até que o usuário informe um valor válido.


if __name__ == '__main__':
    entrada = int(input())
    ancora = True
    while ancora==True:
        if(entrada>=0 and entrada <=10):
            ancora = False
        else:
            print("ENTRADA ERRADA DIGITE NOVAMENTE")
            entrada = int(input())

            
    print("ENTRADA {}".format(entrada))
     