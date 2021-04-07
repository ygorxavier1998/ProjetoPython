#Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10.
#O usuário deve informar de qual numero ele deseja ver a tabuada.
#A saída deve ser conforme o exemplo abaixo:

def tabuada(entradada):
    for x in range(1,11):
        multi = entradada*x
        print("{}x{}={}".format(entradada,x,multi))


if __name__ == '__main__':
    dados = int(input())
    tabuada(dados)