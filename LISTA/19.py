'''
Uma empresa de pesquisas precisa tabular os resultados da seguinte enquete feita a um grande quantidade de organizações:

"Qual o melhor Sistema Operacional para uso em servidores?"

As possíveis respostas são:

1- Windows Server
2- Unix
3- Linux
4- Netware
5- Mac OS
6- Outro

Você foi contratado para desenvolver um programa que leia o resultado da enquete e informe ao final o resultado da mesma. O programa deverá ler os valores até ser informado o valor 0, que encerra a entrada dos dados. Não deverão ser aceitos valores além dos válidos para o programa (0 a 6). Os valores referentes a cada uma das opções devem ser armazenados num vetor. Após os dados terem sido completamente informados, o programa deverá calcular a percentual de cada um dos concorrentes e informar o vencedor da enquete. O formato da saída foi dado pela empresa, e é o seguinte:

Sistema Operacional     Votos   %
-------------------     -----   ---
Windows Server           1500   17%
Unix                     3500   40%
Linux                    3000   34%
Netware                   500    5%
Mac OS                    150    2%
Outro                     150    2%
-------------------     -----
Total                    8800

O Sistema Operacional mais votado foi o Unix, com 3500 votos, correspondendo a 40% dos votos.
'''
import math as math


def stec(info, total ):
    
    for sistema,valor in zip(info.keys(),info.values()):
        print("Sistema Operacional  |    Votos  |    %")
        print("----------------------------------------------")
        print("|{0}-----------------|------{1}-----|-------------|{2:.2f}".format(sistema,valor,((valor/total)*100)))
        print("----------------------------------------------")
       

if __name__ == '__main__':
    SistemasOperacional = ["Windows_Server 0","Unix 0","Linux 0","Netware 0","Mac_OS 0" ,"Outro 0"]
    SistemasOperacionalDic ={}
    cont = 0
    for ope in SistemasOperacional:
          SistemasOperacionalDic[ope.split(" ")[0]] = 0

 
    while(True): 
        entrada = int(input("1 - Windows_Server | 2 - Unix | 3 - Linux |  4 - Netware | 5 - Mac_OS | 6 - Outro - n: \n"))
        
        if(entrada==0):break
        
        if(entrada==1):
            SistemasOperacionalDic['Windows_Server']+=1
            cont+=1
        elif(entrada==2):
              SistemasOperacionalDic['Unix']+=1
              cont+=1
        elif(entrada==3):
            SistemasOperacionalDic['Linux']+=1
            cont+=1
        elif(entrada==4):
            SistemasOperacionalDic['Netware']+=1
            cont+=1
        elif(entrada==5):
              SistemasOperacionalDic['Mac_OS']+=1
              cont+=1
        elif(entrada==6):
              SistemasOperacionalDic['Mac_OS']+=1
              cont+=1

stec(SistemasOperacionalDic,cont)

