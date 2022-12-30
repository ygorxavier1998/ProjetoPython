'''
Foi feita uma estatística em cinco cidades brasileiras para coletar dados sobre acidentes de trânsito. 
Foram obtidos os seguintes dados:
Código da cidade;
Número de veículos de passeio (em 1999);
Número de acidentes de trânsito com vítimas (em 1999). Deseja-se saber:
 
Qual o maior e menor índice de acidentes de transito e a que cidade pertence;
Qual a média de veículos nas cinco cidades juntas;
Qual a média de acidentes de trânsito nas cidades com menos de 2.000 veículos de passeio.

'''


def main():

    Estatistica = {}
    ancora = 2
    while(True):
        CodigoCidade = int(input("Codigo cidade"))
        if CodigoCidade not in Estatistica:
            NumeroVeiculo = int(input("VEICULOS"))
            NumeroAcidente = int(input("ACIDENTES"))
            Estatistica[CodigoCidade] = {'Veiculo':NumeroVeiculo,'Morte':NumeroAcidente}
            
        if(len(Estatistica[CodigoCidade]) > 2):
            break


    print(len())

if __name__ == '__main__':
    main()
