'''
Faça um programa que leia um nome de usuário e a sua senha e não aceite a 
senha igual ao nome do usuário, mostrando uma 
mensagem de erro e voltando a pedir as informações.
'''
def Verific(Login,Senha):
    if(Login==Senha):
        return False
    elif(Login != Senha):
        return True
    


if __name__ == '__main__':
    print("LOGIN:")
    print("SENHA:")
    Login = input().upper()
    Senha = input().upper()
    t = True
    while(t==True):
        
        if(Verific(Login,Senha)==True):
            print("SENHA ACEITA")
            t = False
        elif(Verific(Login,Senha)==False):
            print("LOGIN E SENHA IGUAIS DIGITE NOVAMENTE")
            Login = input().upper()
            Senha = input().upper()
