def retorno(entrada):
    menor = min(entrada)
    maior = max(entrada)
    soma = maior+menor
    return soma

if __name__ == '__main__':
    try:
        exet = 0
        lista = []
        pergunta = 0
        cons = int()

        while(exet==0):
            entrada = int(input())
            if(entrada > 0 or entrada < 1000):
                lista.append(entrada)
                pergunta +=1
                if(pergunta==5):
                    pick = input("DESEJA CONTINUAR? S/N").upper()
                    if(pick=='N'):
                        exet = 1
                    else:
                        pergunta = 0 
        print(retorno(lista))
           
    except ValueError:
        print("SOMENTE INTEIRO")

        