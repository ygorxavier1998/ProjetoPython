
'''
Faça um Progran ma para um caixa eletrônico. O programa deverá perguntar ao usuário a valor
 do saque e depois informar quantas notas de cada valor serão fornecidas. As notas disponíveis serão as
  de 1, 5, 10, 50 e 100 reais. O valor mínimo é de 10 reais e o máximo de 600 reais. O programa não deve 
  se preocupar com a quantidade de notas existentes na máquina.


Exemplo 1: Para sacar a quantia de 
256 reais, o programa fornece
duas notas de 100, uma nota de 50, 
uma nota de 5 e uma nota de 1;

Exemplo 2: Para sacar a quantia de 399 reais,
 o programa fornece três notas de 100, uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1.
'''

def ret(entrada):
    notas = [100,50,10,5,1]
    for x in notas:
        divi = int(entrada/x)
        print("notas de {}----> {}".format(x,divi))
        entrada = entrada%x
       
if __name__ == '__main__':
    try:
        dado = int(input("DIGITE O VALOR A SER SACADO "))
        if(dado>10 and dado<=600):
            ret(dado)
        else:
            print("erro")

    except ValueError:
        tentativas = 2
        while(tentativas > 0):
            print("TENTATIVAS -> {}".format(tentativas-1))
            print("TENTE NOVAMENTE")
            dado = int(input())
            if(dado>10 or dado <=600):
                ret(dado)
            tentativas = 0
    else: 
        print("ERRO DA ENTRADA")
            