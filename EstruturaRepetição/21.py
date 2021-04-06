def Call_back(x):
    number  = x
    if(number%2==0):
        return True
    else:
        return False

if __name__ == '__main__':
    numero = int(input())
    if(Call_back(numero)==False):
        print("PRIMO")
    else:
        print("não primo")
