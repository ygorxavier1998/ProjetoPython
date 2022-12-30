#Faça um programa que leia 5 números e
#nforme a soma e a média dos números.



def maior(dado):

    print("SOMA {}".format(sum(dado)))
    print("MEDIA {}".format(sum(dado)/5))

if __name__ == '__main__':
    lista = []
    for x in range(5):
        entrada = int(input())
        lista.append(entrada)
   
    maior(lista)
