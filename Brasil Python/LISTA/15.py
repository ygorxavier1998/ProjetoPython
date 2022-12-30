'''
Faça um programa que leia um número indeterminado de valores, correspondentes a notas, encerrando a entrada de dados quando for 
informado um valor igual a -1 (que não deve ser armazenado). Após esta entrada de dados, faça:

A - Mostre a quantidade de valores que foram lidos; ok
B - Exiba todos os valores na ordem em que foram informados, um ao lado do outro; OK
C - Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;
D - Calcule e mostre a soma dos valores;
E - Calcule e mostre a média dos valores;
F - Calcule e mostre a quantidade de valores acima da média calculada;
G - Calcule e mostre a quantidade de valores abaixo de sete;
H - Encerre o programa com uma mensagem;

'''
import math as math

def main():
    notas = []
    MaiorQueAMedia = []
    AbaixoSete = []
    while(True):
        nota = float(input("nota aluno:"))
        if(nota < 0):
            break
        else:
            notas.append(nota)
            
    tamanho = len(notas)
    print("A - {}".format(tamanho))
    reverseList = notas[::-1]
    print("B - {}\n".format(notas), end="")
    print("C - {} ".format(notas[::-1]))
    print("D - {} ".format(sum(notas)))
    media = sum(notas)/tamanho
    print("E - {} ".format(media))

    for nota in notas:
        if(nota > media):
            MaiorQueAMedia.append(nota)
        elif(nota < 7):
            AbaixoSete.append(nota)

    print("F - {} ".format(MaiorQueAMedia))
    print("H - {} ".format(AbaixoSete))
    print("ADIOS!!!!!!!")
    

   
if __name__ == '__main__':
    main()