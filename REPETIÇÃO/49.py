 #S = 1/1 + 2/3 + 3/5 + 4/7 + 5/9 + ... + n/m. 
'''
1/1
1+1+1+1
1+3+5
'''

def main():
    repeticao = int(input("REPETIÇÃO"))
    one = 1
    tres= 1
    soma = 0

    for rep in range(repeticao):
        print("{}/{}".format(one,tres))
        one += 1
        tres +=2
        soma += (tres+one)
    print(soma)
if __name__ == '__main__':
    main()
    