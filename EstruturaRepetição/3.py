'''
Faça um programa que leia e valide as seguintes informações:
.
Nome: maior que 3 caracteres;
Idade: entre 0 e 150;
Salário: maior que zero;
Sexo: 'f' ou 'm';
Estado Civil: 's', 'c', 'v', 'd';
'''
def ValidNome(nome):
    t = len(nome)
    if(t>3):
        return True
    else:
        return False

def ValidIdade(idade):
    i = idade
    if(i > 0 and i<=150):
        return True
    else:
        return False

def ValidSalario(Salario):
    s = Salario
    if(Salario > 0):
        return True
    else:
        return False

def ValidSexo(Sexo):
    s = Sexo
    if(s=="f" or s=="m"):
        return True
    else:
        return False

def EstadoCivil(EC):
    Estado_Civil =["s", "c", "v", "d"]
    S = str(EC)
    for x in Estado_Civil:
        if(x==S):
            return True
    else:
        return False


if __name__ == '__main__':
    ancora = 5
    while (ancora > 0):
        print("DIGITE SEU NOME")
        nome = input()
        if(ValidNome(nome)==False):
            print("NOME INVALIDO DIGITE NOVAMENTE")
            nome = input()
            V = ValidNome(nome)
        elif(ValidNome(nome)==True):
            print("NOME VALIDO\n")
            ancora -=1
            
        print("DIGITE SUA IDADE")
        idade = int(input())
        if(ValidIdade(idade)==True):
            print("IDADE VALIDA \n")
            ancora -=1
        elif(ValidIdade(idade)==False):
            print("IDADE INCORRETA DIGITE NOVAMENTE")
            idade = int(input())


        print("DIGITE SEU SALARIOI")
        Salario = float(input())
        if(ValidSalario(Salario)==True):
            print("SALARIO VALIDO")
            ancora -=1
        elif(ValidSalario(Salario)==False):
            print("SALARIO INCORRETA DIGITE NOVAMENTE")
            Salario = float(input())
        
        print("DIGITE SEU SEXO  F OU M ")
        Sexo = input().lower()
        if(ValidSexo(Sexo)==True):
            print("SEXO VALIDO")
            ancora -=1
        elif(ValidSexo(Sexo)==False):
            print("SEXO INCORRETA DIGITE NOVAMENTE")
            Sexo = input().lower()

        print("ESTADO CIVIL ['s', 'c', 'v', 'd']")
        C = input()
        if(EstadoCivil(C)==True):
            print("ESTADO CIVIL VALIDO")
            ancora -=1
        elif(EstadoCivil(C)==False):
            print("ESTADO CIVIL INVALIDO")
            EstadoCivil = input("?")

        print(" NOME {}\n IDADE-->{} \n Salario-->{}\n Sexo-->{}\n EstadoCivil-->{}".format(nome,idade,Salario,Sexo,C))
        