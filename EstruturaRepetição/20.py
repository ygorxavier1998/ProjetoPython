#Altere o programa de cálculo do fatorial, permitindo ao usuário calcular o fatorial várias vezes 
#e limitando o fatorial a números inteiros positivos e menores que 16.



def retorno(entrada):
    multi = 0
    termi = 1
    for x in range(entrada,1,-1):
        if termi == 1:
            multi = x
            termi -=1  # ANCORA PARA O PRIMEIRA DODAD
        else: 
           multi =  multi*x
           print(multi)
        


if __name__ == '__main__':
    t = True
    while(t==True):
        entrada = int(input())
        if(entrada > 0 and entrada <= 16):
            retorno(entrada)
        else:
            print("ENTRADA NÃO ACEITA")
            t = False
    