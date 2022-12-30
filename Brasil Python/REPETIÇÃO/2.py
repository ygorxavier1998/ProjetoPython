#Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando 
#uma mensagem de erro e voltando a pedir as informações.




def Veri_Log(login,senha):
    l = login
    s = senha
    #RETIRADA DE ESPAÇO EM BRANCO
    l.replace(" ","")
    s.replace(" ","")
    if(l==s):
        return  True
    elif(l!=s):
        return  False

if __name__ == '__main__':
    log = input("login....")
    se = input("Senha....")
    verifica = Veri_Log(log,se)
    if(verifica == False):
        print("senhas diferente")
    while(verifica == True):
        print("LOGIN E SENHA IGUAIS,repita")
        log = input()
        se = input()
        verifica = Veri_Log(log,se)
    print("login aceito\nsenha aceita")