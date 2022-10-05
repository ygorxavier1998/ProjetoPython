'''
Utilize uma lista para resolver o problema a seguir. Uma empresa paga seus vendedores com base em comissões. 
O vendedor recebe $200 por semana mais 9 por cento de suas vendas brutas daquela semana. Por exemplo,
um vendedor que teve vendas brutas de $3000 em uma semana recebe $200 mais 9 por cento de $3000, ou seja, um total de $470.
Escreva um programa (usando um array de contadores) que determine quantos vendedores receberam salários nos seguintes intervalos de valores:

$200 - $299 = j
$300 - $399 = h
$400 - $499 = g
$500 - $599 = f
$600 - $699 = e
$700 - $799 = d
$800 - $899 = c 
$900 - $999 = b
$1000 em diante = a 
Desafio: Crie ma fórmula para chegar na posição da lista a partir do salário, sem fazer vários ifs aninhados.

'''



from ast import If


def cal(Valor):
    for item in Valor.items():
        print(item)    
   
if __name__ == '__main__':
    ListaValor = {"a":0 , "b":0 ,"c":0 ,"d":0 ,"e":0 ,"f":0 ,"g":0 ,"h":0 ,"j":0}
    entrada = int(input())
    
    while(entrada != 1 ):   
        entrada = int(input())
          
        if(entrada >= 1000):
            ListaValor["a"] +=1

        elif(entrada >= 200 and entrada <= 299):
            ListaValor["j"] +=1

        elif(entrada >= 300 and entrada <= 399):
            ListaValor["h"] +=1
                
        elif(entrada >= 400 and entrada <= 499):
            ListaValor["g"] +=1

        elif(entrada >= 500 and entrada <= 599):
            ListaValor["f"] +=1
        
        elif(entrada >= 600 and entrada <= 699):
            ListaValor["e"] +=1

        elif(entrada >= 700 and entrada <= 799):
            ListaValor["d"] +=1

        elif(entrada >= 800 and entrada <= 899):
            ListaValor["c"] +=1
        
        elif(entrada >= 900 and entrada <= 999):
            ListaValor["b"] +=1
      

        if(entrada == 1):
            break

    cal(ListaValor)