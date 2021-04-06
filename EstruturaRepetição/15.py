# série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,...
#Faça um programa capaz de gerar a série até o n−ésimo termo.


if __name__ == '__main__':
    a = 1
      
    for x in range(50):
        if(x==0):
            c = a
        elif(x==1):
            c = b
        else:
            c = a+b
            a = b
            b = c
            print(c)
        
