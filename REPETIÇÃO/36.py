
#Desenvolva um programa que faça a tabuada de um número qualquer inteiro que será digitado pelo usuário,
#mas a tabuada não deve necessariamente iniciar em 1 e terminar em 10, o valor inicial e final devem ser informados 
#também pelo usuário, conforme exemplo abaixo:

def Tabuada(Numero,Comeco,fim):
    try:
        while(Comeco <= fim):
            print("{} x {} = {}".format(Numero,Comeco,(Numero*Comeco)))
            Comeco += 1
    except BaseException:
        print("erro")


if __name__ == '__main__':
    NumeroTabuada = int(input())
    Comeco = int(input())
    Fim = int(input())
    if(Comeco < Fim):
         Tabuada(NumeroTabuada,Comeco,Fim)

    else:
        print("Entrada errada")
   
