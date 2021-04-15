
#A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,... 
#Faça um programa capaz de gerar a série até o n−ésimo termo.


def fibo():
    futuro = 0
    presente = 0
    passado = 0
    for x in range(10):
        if(x==0):
            passado += 0
        if(x==1):
            presente += 1
        futuro = presente+passado
        presente = passado
        passado = futuro
        #presente = passado
        #print("presente{} \n passado{} \n futuro{}".format(presente,passado,futuro))
        print("{} {}".format(x,futuro))
        

if __name__ == '__main__':
    fibo()