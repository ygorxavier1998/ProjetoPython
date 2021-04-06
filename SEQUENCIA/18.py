#Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps),
#calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).

def retorno(arquivo):
    print("TAMAMHO EM Mb {}".format(arquivo*8))
    print("TEMPO NECESSARIO PARA TRANSFERENCIA EM byts/segundo {}".format(arquivo / 60))



if __name__ == '__main__':
    Tamanho_Arquivo = int(input())
    retorno(Tamanho_Arquivo)
