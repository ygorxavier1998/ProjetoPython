'''
Supondo que a população de um país A seja da ordem de 80000 
habitantes com uma taxa anual de crescimento de 3% e que a população de B seja 200000 
habitantes com uma taxa de crescimento de 1.5%. Faça um programa que calcule e escreva o número de 
anos necessários para que a população do país A ultrapasse ou iguale a população do país B, mantidas as 
taxas de crescimento.

PopulacaoA = 80000
TaxaA = 3%
PopulacaoB = 200000
TaxaB = 1.5%

'''
def TaxaCescimento(PopulacaoA,PopulacaoB,TaxaA,TaxaB):
    clico = 0
    while(PopulacaoA <= PopulacaoB):
        PopulacaoA = PopulacaoA+(PopulacaoA*TaxaA)
        PopulacaoB = PopulacaoB+(PopulacaoB*TaxaB)
        clico += 1
    print("POPULAÇÃO A-->{}".format(PopulacaoA))
    print("POPULAÇÃO B-->{}".format(PopulacaoB))
    print("TAXA A {} \nTAXA B {} ".format((TaxaA*100),(TaxaB*100)))
    print("ANOS NECESSARIOS {}".format(clico))




if __name__ == '__main__':
    PopuA = int(input())
    PopuB = int(input())
    TaxaA = float(input())
    TaxaB = float(input())
    
    TaxaCescimento(PopuA,PopuB,(TaxaA/100),(TaxaB/100))

