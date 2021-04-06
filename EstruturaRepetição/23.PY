#Faça um programa que mostre todos os primos entre 1 e N sendo N um número inteiro fornecido pelo usuário.
# O programa deverá mostrar também o número de divisões que ele executou para encontrar os números primos.
# Serão avaliados o funcionamento, o estilo e o número de testes (divisões) executados.

def fat(dado):
    mmc = 2
    numero = dado
    for x in range(int(1),dado):
        resultado = numero/mmc
        tipo =  type(resultado)
        if(tipo==int or resultado==1):
            print("---->RESULTADO {}\n---->MMC {}".format(resultado,x))
            resultado = resultado/mmc
            if(type(resultado/mmc) != int):
                mmc += 1

if __name__ == '__main__':
    entrada = int(input())
    fat(entrada)