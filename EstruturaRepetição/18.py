#Faça um programa que, dado um conjunto de N números,
# determine o menor valor, o maior valor e a soma dos valores.
def retorno(entrada):
    menor = min(entrada)
    maior = max(entrada)
    soma = maior+menor
    return soma

if __name__ == '__main__':
    exet = 0
    lista = []
    pergunta = 0
    while(exet==0):
        entrada = int(input())
        lista.append(entrada)
        pergunta +=1

        if(pergunta==5):
            pick = input("DESEJA CONTINUAR? S/N").upper()
            if(pick=='N'):
                exet = 1
            else:
                pergunta = 0 
    print(retorno(lista))
            #pick = input("PARA SAIDA DIGITE E").upper()
        