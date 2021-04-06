#Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever:
#F - Feminino, M - Masculino, Sexo Inválido.


def escolha (x):
    if(x=='F'):
        print("FEMININO")
    elif(x=='M'):
        print("MASCULINO")
    else:
        print("ESCOLHA INCORRETA")


if __name__ == '__main__':
    pick = input()
    escolha(pick)