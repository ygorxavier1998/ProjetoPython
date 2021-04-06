#Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10.]
#O usuário deve informar de qual numero ele deseja ver a tabuada.
#A saída deve ser conforme o exemplo abaixo:


def Tabuada(firt):
    for x in range(11):
        multi = firt * x 
        print("{} x {} = {}".format(firt,x,multi))

if __name__ == '__main__':

    x = int(input())
    if(x >= 0 and x<=10):
        Tabuada(x)
    else:
        print("ERRADO ")