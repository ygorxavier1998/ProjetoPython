#Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores. Peça 
#para cada eleitor votar e ao final mostrar o número de votos de cada candidato.

#   dicionarios

# estrututa
    # x = {chave:valor}


# 45 - MAICON
# 69 - JUNIO
# 41 - FELIPE


if __name__ == '__main__':
    dic = {
            'MAICON': 0,
            'JUNIOR': 0,
            'FELIPE': 0
         }
   
    QuantidadeCandidato = int(input("QUANTIDADE DE ELEITORES \n"))
    while(QuantidadeCandidato > 0):
        print("CANDIDATOS DISPONIVEIS")
        print("45 - maicon \n 69 - JUNIO \n 41 - FELIPE")
        voto = int(input())
        if(voto==45):
            dic['MAICON'] += 1
            QuantidadeCandidato -= 1
        elif(voto==69):
            dic['JUNIOR'] += 1
            QuantidadeCandidato -= 1
        elif(voto==41):
            dic['FELIPE'] += 1
            QuantidadeCandidato -= 1
        else:
            print("ENTRADA ERRADA")
    
    for x in dic.keys():
        print(x,"-->",dic[x])
    