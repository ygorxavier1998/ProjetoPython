'''

Faça um programa que carregue uma lista com os modelos de cinco carros
(exemplo de modelos: FUSCA, GOL, VECTRA etc). 
Carregue uma outra lista com o consumo desses carros, isto é, quantos quilômetros cada um desses carros faz com um litro de combustível. Calcule e mostre:
modelo do carro mais econômico;
Quantos litros de combustível cada um dos carros cadastrados consome para percorrer uma distância de 1000 quilômetros e quanto isto custará, considerando um que a gasolina custe R$ 2,25 o litro. Abaixo segue uma tela de exemplo. O disposição das informações deve ser o mais próxima possível ao exemplo. Os dados são fictícios e podem mudar a cada execução do programa. 
'''
#LITRO DA GASOSA 2.25 R$

def calc(carros,consumos):
         for carro in range(len(carros)):
            consumoMedio = 1000/consumos[carro]
            preco = (consumoMedio)*2.25
            
            print("{0} - {1}  -  {2} - {3:.2f} - {4:.2f}".format(carro, carros[carro] , consumos[carro],consumoMedio,preco))

if __name__ == '__main__':
    carros = []
    consumo = []
    numero = 0
    while(True):
        numero+=1
        carro  = input("Veiculo: {}\n".format(numero))
        if(carro == "Exit"):break
        consumoIndividual = float(input("Km por litro: "))
        carros.append(carro)
        consumo.append(consumoIndividual)

    calc(carros,consumo)