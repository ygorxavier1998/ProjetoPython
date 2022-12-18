'''
Sua organização acaba de contratar um estagiário para trabalhar no Suporte de Informática,
com a intenção de fazer um levantamento nas sucatas encontradas nesta área. A primeira tarefa 
dele é testar todos os cerca de 200 mouses que se encontram lá, testando e anotando o estado de 
cada um deles, para verificar o que se pode aproveitar deles.
Foi requisitado que você desenvolva um programa para registrar este levantamento. O programa deverá receber
um número indeterminado de entradas, cada uma contendo: um número de identificação do mouse o tipo de defeito:
necessita da esfera;
necessita de limpeza; a.necessita troca do cabo ou conector; a.quebrado ou inutilizado Uma identificação igual a
zero encerra o programa. Ao final o programa deverá emitir o seguinte relatório:

'''

def calc(problemas):
    tamanho = len(problemas)
    
    problema_Dic = {"1":0,"2":0,"3":0,"4":0}
    for item in problemas:
        if(int(item))==1:
            problema_Dic["1"] += 1
        elif(int(item))==2:
            problema_Dic["2"] += 1
        elif(int(item))==3:
            problema_Dic["3"] += 1
        elif(int(item))==4:
            problema_Dic["4"] += 1

    primeiro =  (problema_Dic["1"])
    segundo = (problema_Dic["2"])
    terceiro =  (problema_Dic["3"])
    quarto =  (problema_Dic["4"])
    print(tamanho)
    print("Situação | Quantidade | Percentual")
    print("1 - necessita da esfera | {0} | {1}".format(primeiro,((primeiro/tamanho)*100)))
    print("2 - necessita de limpeza  | {0} | {1}".format(segundo,((segundo/tamanho)*100)))
    print("3 - necessita troca do cabo ou conector  | {0} | {1}".format(terceiro,((terceiro/tamanho)*100)))
    print("4 - quebrado ou inutilizado | {0} | {1}".format(quarto,((quarto/tamanho)*100)))
   


if __name__ == '__main__':
    problemas = []
    while(True):
        entrada  = int(input("1-necessita da esfera\n2-necessita de limpeza\n3-necessita troca do cabo ou conector\n4-quebrado ou inutilizado:\n"))
        if(entrada==0):break
        problemas.append(entrada)
        
    calc(problemas)