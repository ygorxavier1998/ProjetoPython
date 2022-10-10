'''
Em uma competição de salto em distância cada atleta tem direito a cinco saltos. O resultado do atleta será determinado pela média dos cinco valores restantes.
 Você deve fazer um programa que receba o nome e as cinco distâncias alcançadas pelo atleta em seus saltos e depois informe o nome, os saltos e a média dos saltos. 
 O programa deve ser encerrado quando não for informado o nome do atleta. A saída do programa deve ser conforme o exemplo abaixo:

Atleta: Rodrigo Curvêllo
Primeiro Salto: 6.5 m
Segundo Salto: 6.1 m
Terceiro Salto: 6.2 m
Quarto Salto: 5.4 m
Quinto Salto: 5.3 m

Resultado final:
Atleta: Rodrigo Curvêllo
Saltos: 6.5 - 6.1 - 6.2 - 5.4 - 5.3
Média dos saltos: 5.9 m

'''



def calc(atleta):
    for nome,valor in zip(atleta.keys(),atleta.values()):
        print("Resultado final")
        print("Atleta:{}".format(nome))
        print("Saltos {}".format(valor))
        print("Media dos saltos {}".format(sum(valor)/5))
        

def main():
    atletas = {}
    salto = []
    print("Digite o nome do atleta")
    nome = input("nome: ")

    while(nome != ""):
        for x in range(0,4):
            print("Salto:")
            entrada = float(input())
            salto.append(entrada)

        atletas[nome] = salto
        calc(atletas)
        nome = input("nome: ")
        salto = []


if __name__ == '__main__':
    main()