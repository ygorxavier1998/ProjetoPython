def main():
    repeticao = int(input("REPETIÇÃO"))
    one = 1
    dois= 2
    soma = 0

    for rep in range(repeticao):
        print("{}/{}".format(one,dois))
        dois += 1
        soma += (one+dois)
    print(soma)
    
if __name__ == '__main__':
    main()
    