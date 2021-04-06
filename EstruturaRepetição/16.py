#A série de Fibonacci é formada pela seqüência 0,1,1,2,3,5,8,13,21,34,55,...
#Faça um programa que gere a série até que o valor seja maior que 500.


if __name__ == '__main__':
    a = 1
    c = 0   
    x = 0  
    b = 0
    while c < 500:
        if(x==0):
            c = a
            x +=1
            print("-->INDEX {}--->VALOR {}".format(x,c))
        elif(x==1):
            c = b
            x += 1
            print("-->INDEX {}--->VALOR {}".format(x,c))
        else:
            c = a+b
            a = b
            b = c
            x += 1
            print("-->INDEX {}--->VALOR {}".format(x,c))

