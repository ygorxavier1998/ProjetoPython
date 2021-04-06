#Faça um programa que peça dois números, base e expoente, calcule e mostre o primeiro número elevado ao segundo número. 
#Não utilize a função de potência da linguagem.



def Expo(Base,Expo):
    return base**Expo

if __name__ == '__main__':  
    base = int(input())
    Expoente = int(input())
    print(Expo(base,Expoente))