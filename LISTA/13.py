#Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma lista.
#Após isto, calcule a média anual das temperaturas e mostre todas 
#as temperaturas acima da média anual,
#e em que mês elas ocorreram (mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . ).
def main():
    temperaturaMediaMeses = []
    meses = ["Janeiro","fevereiro","Março","Maio","Abril","junho","julho","agosto","setembro","outubro","novembro","dezembro"]
    
    for tempe in range(0,11,1):
        print("MES:{}".format(meses[tempe]))
        var_Tempe = float(input("Digite a temperatura: "))
        temperaturaMediaMeses.append(var_Tempe)
        
    mediaTemperatura  = sum(temperaturaMediaMeses)/11;
    print("A media foi: {}".format(mediaTemperatura))
    

    naoMaior = True
    
    for tempe in  range(0,11,1):
        if(mediaTemperatura > temperaturaMediaMeses[tempe]):
            naoMaior = False
            print("O mes que superou a media:{}".format(meses[tempe]))
            
    if(naoMaior==True):
        print("Não houve temperatura maior que a media")
        
        
if __name__ == '__main__':
    main()