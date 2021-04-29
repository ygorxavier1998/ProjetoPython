#Faça um programa que peça para n pessoas a sua idade, ao final o programa
#devera verificar se a média de idade da turma varia entre 0 e 25,26 e 60 e maior que 60; e então, dizer 
#se a turma é jovem, adulta ou idosa, conforme a média calculada.






def Media(idade):
    tamanho = len(idade)
    soma = sum(idade)
    return soma/tamanho


if __name__ == '__main__':
    print("PROGRAMA IDADE ")
    Quanti_Notas = int(input("quantidade de pessoas"))
    #
    lista = []
    entrada  = 0
    while(Quanti_Notas != 0):
        nota1 = float(input("\n"))
        lista.append(nota1)
        Quanti_Notas -= 1

    IdadeMedia  = Media(lista)
    if(IdadeMedia <= 25):
        print("JOVEM")
    elif(IdadeMedia > 25 and IdadeMedia <60):
        print("ADULTA")
    elif(IdadeMedia < 60):
        print("IDOSA")
        