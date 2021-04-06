'''Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um
triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
Dicas:

Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
Triângulo Equilátero: três lados iguais;
Triângulo Isósceles: quaisquer dois lados iguais;
Triângulo Escaleno: três lados diferentes;

'''

def Retangulo(a,b,c):

    if((a+b)>c and (a+c)>b and (c+b)>a):
        print("Triângulo")
        if(a==b and b==c):
            return print("Triângulo Equilátero")
             

#------------------------------ISOSCELES----------------------------------------#
        if (Lado1 == Lado2):
            Vec1 = (Lado1 == Lado2)
            if (Vec1 != Lado3):
                return print("Triângulo Isósceles")

        elif (Lado2 == Lado3):
            Vec2 = (Lado2 == Lado3)
            if (Vec2 != Lado1):
                return print("Triângulo Isósceles")

        elif (Lado3 == Lado1):
            Vec3 = (Lado3 == Lado1)
            if (Vec3 != Lado2):
                return print("Triângulo Isósceles")
# ----------------------------ESCALENO----------------------------------------#
        if (Lado1 != Lado2):
            Escaleno1 = (Lado1 != Lado2)
            if(Escaleno1 != Lado3):
                return print("TRIANGULO ESCALENO")
  
        elif (Lado2 != Lado3):
            Escaleno2 = (Lado2 != Lado3)
            if(Escaleno2 != Lado1):
                return print("Triângulo Escaleno")

        elif (Lado3 != Lado1):
            Escaleno3 = (Lado3 != Lado1)
            if(Escaleno3 != Lado2):
                return print("Triângulo Escaleno")
    else:
        return print("NÃO TRIANGULO")


            
            
if __name__ == '__main__':

    Lado1 = int(input())
    Lado2 = int(input())
    Lado3 = int(input())
    
    Retangulo(Lado1,Lado2,Lado3)