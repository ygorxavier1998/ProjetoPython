'''Faça um programa que leia e valide as seguintes informações:
Nome: maior que 3 caracteres;
Idade: entre 0 e 150;
Salário: maior que zero;
Sexo: 'f' ou 'm';
Estado Civil: 's', 'c', 'v', 'd';
'''

def valid(nome,idade,salario,sexo,Estado_Civil):
#VALIDAÇÃO DE NOME TAMANHO MAIOR 3
    Tamanho_Nome = len(nome)
    Var_Verifica = 0
    if(Tamanho_Nome <= 3):
        print("NOME INVALIDO")
    elif(Tamanho_Nome > 3):
        print("NOME VALIDO")
        Var_Verifica +=1

    if(idade >=0 and idade<=150):
        print("IDADE VALIDA")
        Var_Verifica +=1
    else:
        print("IDADE INVALIDA")

    if(salario > 0):
        print("SALARIO ACEITO")
        Var_Verifica +=1
    elif(salario < 0):
        print("SALARIO NÃO ACEITO")

    if(sexo=="M" or sexo=="F"):
        print("SEXO ACEITO ACEITO")
        Var_Verifica +=1
    else:
        print("sexo não aceito")
    if(Estado_Civil=="S",
       Estado_Civil=="C",
       Estado_Civil=="V",
       Estado_Civil=="D"):
        Var_Verifica += 1
    else:
        print("ESTADO INVALIDO")

    return Var_Verifica



if __name__ == '__main__':
    nome = input("DIGITE SEU NOME")
    idade = int(input("DIGITE SUA IDADE"))
    salario = float(input("DIGITE SEU SALARIO"))
    sexo = input("SEXO M OU F").upper()
    Estado_Civil = input("Estado Civil: 's', 'c', 'v', 'd' ").upper()

    while(valid(nome,idade,salario,sexo,Estado_Civil) != 5):
        nome = input("DIGITE SEU NOME")
        idade = int(input("DIGITE SUA IDADE"))
        salario = float(input("DIGITE SEU SALARIO"))
        sexo = input.upper("SEXO M OU F")
        Estado_Civil = input.upper("Estado Civil: 's', 'c', 'v', 'd'")
        valid(nome,idade,salario,sexo,Estado_Civil)


    