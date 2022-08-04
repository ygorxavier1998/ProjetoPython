#Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes. 
# A E I O U 
def verifica(list):
    vogalVet = ["a" ,"e","i","o","u"]
    contConsoante = 0
    vetConsoanteNew = []
    for x in list:
        if(x in vogalVet):
            pass
        else:
            contConsoante += 1 
            vetConsoanteNew.append(x)
    print("o valor de consoantes lidas {}".format(contConsoante))
    print("{}".format(vetConsoanteNew))

def main():
    vetcaracter = []
    entrada = input("digite os caracteres ")
    if(len(entrada) <= 10):
        for x in entrada:
            vetcaracter.append(x)
        verifica(vetcaracter)
    else:
        while(True):
            print("entrada não aceita digite novamente")
            entrada = input("digite os caracteres ")
            if(len(entrada) <= 10):
                for x in entrada:
                    vetcaracter.append(x)
                verifica(vetcaracter)
                break
            else:
                    continue


if __name__ == '__main__':
    main()
    