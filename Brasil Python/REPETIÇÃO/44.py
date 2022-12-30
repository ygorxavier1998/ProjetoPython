'''
1 , 2, 3, 4  - Votos para os respectivos candidatos 
(você deve montar a tabela ex: 1 - Jose/ 2- João/etc)
5 - Voto Nulo
6 - Voto em Branco
'''

from prettytable import PrettyTable

def main():
    votos = {'1':0,'2':0,'3':0,'4':0,'5':0,'6':0}
    tabela = PrettyTable()
    TabelaVotosFinal = PrettyTable()
    tabela.add_row(["1 - jose","2 - joão","3 - perna de pau",
    "4 - naris de pika-pau","5 - vato nulo","6 - voto branco"])
    print(tabela)
    while(True):
        codigo = int(input("CODIGO:"))
        if(codigo==0):
            break
        if(str(codigo) not in votos.keys()):
            print("codigo errado, digite novamente")
            codigo = int(input("CODIGO:"))
        else:
            pass
        if(codigo==1):
            votos['1'] += 1
        elif(codigo==2):
            votos['2'] += 1

        elif(codigo==3):
            votos['3'] += 1

        elif(codigo==4):
            votos['4'] += 1

        elif(codigo==5):
            votos['5'] += 1

        elif(codigo==6):
            votos['6'] += 1

    TotalEstatistica = sum(votos.values())
    VotosBrnco = votos['6']
    VotosNulos = votos['5']
    TotalBrancoPorcento = ((VotosBrnco/TotalEstatistica)*100)
    TotalNulosPorcento = ((VotosNulos/TotalEstatistica)*100)
   
    TabelaVotosFinal.add_row(["1 - votos jose:",votos['1'],"2 - votos joão:",votos['2'],"3 - votos perna de pau:",votos['3'],
    "4 - votos joão:",votos['4'],"5 - votos joão:",votos['5'],"6 - votos joão:",votos['6']])
    print(TabelaVotosFinal)
    print("Porcentagem de votos Brancos: {} \n   Porcentagem de votos Nulos {}".format(TotalBrancoPorcento,TotalNulosPorcento))
if __name__ == '__main__':
    main()
