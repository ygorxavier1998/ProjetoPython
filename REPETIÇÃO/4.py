'''
Supondo que a população de um país A seja da ordem de 80000 habitantes com uma 
taxa anual de crescimento de 3% e que a população de B seja 200000 habitantes com uma 
taxa de crescimento de 1.5%. Faça um programa que calcule e escreva o número de anos
 necessários para que a população do país 
A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento.
'''


def Populacao():
    PopulacaoA = 80000
    TaxaA = 0.03
    PopulacaoB = 200000
    TaxaB = 0.0015
    conte = 0
    while(PopulacaoB >= PopulacaoA):
        print("POPULAÇÃO A--->{}\nPOPULAÇÃO B--->{}".format(PopulacaoA,PopulacaoB))
        PopulacaoA += PopulacaoA*TaxaA
        PopulacaoB +=PopulacaoB*TaxaB
        conte +=1
        
    print("POPULAÇÃO A--->{}\nPOPULAÇÃO B--->{}".format(PopulacaoA,PopulacaoB))
    print("A QUANTIDADE NECESSARIA {}".format(conte))


if __name__ == '__main__':
    Populacao()