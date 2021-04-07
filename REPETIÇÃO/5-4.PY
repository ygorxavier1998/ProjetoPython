'''
Supondo que a população de um país A seja da ordem de 80000 habitantes com uma 
taxa anual de crescimento de 3% e que a população de B seja 200000 habitantes com uma 
taxa de crescimento de 1.5%. Faça um programa que calcule e escreva o número de anos
 necessários para que a população do país 
A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento.
'''
#Altere o programa anterior permitindo ao 
# usuário informar as 
# populações e as 
#Taxas de crescimento iniciais. 
#Valide a entrada e permita repetir a operação.

def Populacao(p1,p2,t1,t2):
    PopulacaoA = p1
    TaxaA = t1/100
    PopulacaoB = p2
    TaxaB = t2/100
    conte = 0
    while(PopulacaoB >= PopulacaoA):
        print("POPULAÇÃO A--->{}\nPOPULAÇÃO B--->{}".format(PopulacaoA,PopulacaoB))
        PopulacaoA += PopulacaoA*TaxaA
        PopulacaoB +=PopulacaoB*TaxaB
        conte +=1
        
    print("POPULAÇÃO A--->{}\nPOPULAÇÃO B--->{}".format(PopulacaoA,PopulacaoB))
    print("A QUANTIDADE NECESSARIA {}".format(conte))


if __name__ == '__main__':
    PopA = int(input())
    PopB = int(input())
    TaxaA = float(input())
    TaxaB = float(input())
    Populacao(PopA,PopB,TaxaA,TaxaB)