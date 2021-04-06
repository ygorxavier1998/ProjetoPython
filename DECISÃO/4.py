#Faça um Programa que verifique se uma letra digitada é vogal ou consoante.


def Pick(x):
    vogal = ["a","e","i","o","u"]
    for i in vogal:
        if i == x:
            print("VOGAL {}".format(i))
            break
    else:
        print("CONSOANTE {}".format(x))

if __name__ == '__main__':
    entrata = input()
    Pick(entrata)