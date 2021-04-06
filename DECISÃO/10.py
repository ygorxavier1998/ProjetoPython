#Faça um Programa que pergunte em que turno você estuda. Peça para digitar
#M-matutino ou V-Vespertino ou N- Noturno. Imprima a mensagem
#"Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.
def Mensagem(Pick):
    if(Pick=='M'):
        return print("BOM DIA")
    elif(Pick=='V'):
        return print("BOM TARDE")
    elif(Pick=='N'):
        return print("BOA NOITE")

if __name__ == '__main__':
    Entrada = input()

    Mensagem(Entrada)