'''
Uma academia deseja fazer um senso entre seus clientes para descobrir o mais alto, o 
mais baixo, a mais gordo e o mais magro, para isto você deve fazer um programa que pergunte a 
cada um dos clientes da academia seu código, sua altura e seu peso. O final da digitação de dados deve 
ser dada quando o usuário digitar 0 (zero) no campo código. Ao encerrar o programa também deve ser informados 
os códigos e valores do clente mais alto, do mais baixo, do mais gordo e do mais magro,
além da média das alturas e dos pesos dos clientes
'''
def main():
    aluno = { }
    codigo = int()
    altura = float()
    peso = float()

    while(True):
        print("SEJA BEM VINDA A ACADEMIA 2KJ")
        codigo = int(input("DIGITE SEU CODIGO\t"))
        if(codigo==0):
            break

        altura = float(input("SEU ALTURA\t"))
        peso = float(input("SEU PESO\t"))
        if(codigo not in aluno.keys()):
            aluno[codigo] = [altura,peso]

    Estatisficas(aluno)

def Estatisficas(lista):
    MaiorPeso = 0
    MaiorAltura = 0
    MediaPeso = 0
    MedioAltura = 0
    for x in lista.keys():
        if(lista[x][1] > MaiorPeso):
            MaiorPeso = lista[x][1]

        MediaPeso += (lista[x][1])/len(lista)

        if(lista[x][0] > MaiorAltura):
            MaiorAltura = lista[x][0]

        MedioAltura += (lista[x][0])/len(lista)

    print("MAIOR PESO: ",MaiorPeso)
    print("MAIOR ALTURA:",MaiorAltura)
    print("MEDIA ALTURA:",MedioAltura )
    print("MEDIA PESO:",MediaPeso)


if __name__ == '__main__':
    main()
    

