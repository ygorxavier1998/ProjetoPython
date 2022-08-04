'''
//Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada informação no seu respectivo vetor. 
//Imprima a
//idade e a altura na ordem inversa a ordem lida. 
'''

from dis import dis


def main():
    altura = []
    idade = []
    for x in range(1,3,1):
        AlturaEntrada = float(input("Altura"))
        altura.append(AlturaEntrada)
        IdadeEntrada = int(input("Idade"))
        idade.append(IdadeEntrada)
   
    print("Ordem normal {} {}".format(altura,idade))
    
    print("ordem inversa {} {}".format(altura[::-1],idade[::-1]))
    
if __name__ == '__main__':
    main()
    