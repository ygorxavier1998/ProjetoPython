import statistics as st
def main():
    nome  = str
    saltos = []
    nome = input("Digite o nome do atleta ")
    for x in range(1,8,1):
        SaltoAtleta  = float(input("nota do Juiz N°--> {} ".format(x)))
        saltos.append(SaltoAtleta)
    
    MaiorPosicao = max(saltos)
    MenorPosicao = min(saltos)
    print("--> maior ",MaiorPosicao)
    print("--> menor ",MenorPosicao)
    saltos.pop(saltos.index(max(saltos)))
    saltos.pop(saltos.index(min(saltos)))
    print(st.mean(saltos))
    
if __name__ == '__main__':
    main()
    
