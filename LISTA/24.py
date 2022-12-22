'''
Faça um programa que simule um lançamento de dados.
Lance o dado 100 vezes e armazene os resultados em um vetor . 
Depois, mostre quantas vezes cada valor foi conseguido. 
Dica: use um vetor de contadores(1-6) e uma função para gerar numeros aleatórios, 
simulando os lançamentos dos dados. 

'''
import random as ran
def aleatorio():
    dataAleatorio = []
    numeroAleatoriaDic = {"1":0,"2":0,"3":0,"4":0,"5":0,"6":0}
    for interation in range(100):
        numeroAleatoria = ran.randint(1,6)
        dataAleatorio.append(numeroAleatoria)
    
    for numero in dataAleatorio:
        if((numero)==1):numeroAleatoriaDic["1"]=+1
        elif((numero)==2):numeroAleatoriaDic["2"]+=1
        elif((numero)==3):numeroAleatoriaDic["3"]+=1
        elif((numero)==4):numeroAleatoriaDic["4"]+=1
        elif((numero)==5):numeroAleatoriaDic["5"]+=1
        elif((numero)==6):numeroAleatoriaDic["6"]+=1
        
    print(dataAleatorio)
    print(numeroAleatoriaDic)
        
if __name__ == '__main__':
    print(aleatorio())