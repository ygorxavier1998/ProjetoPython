'''
O Sr. Manoel Joaquim expandiu seus negócios para além dos negócios de 1,99 e agora possui uma loja de conveniências.
 Faça um programa que implemente uma caixa registradora rudimentar. O programa deverá receber um número desconhecido de 
 valores referentes aos preços das mercadorias. Um valor zero deve ser informado pelo operador para indicar o final da
compra. O programa deve então mostrar o total da compra e perguntar o valor em dinheiro que o cliente forneceu, para
então calcular e mostrar o valor do troco. Após esta operação, o programa deverá voltar ao ponto inicial, para 
registrar a próxima compra. A 
'''

def NotaFiscal(produtos,TotalPagar,Troco):
    print("-------------------NOTA FISCAL-------------------")
    codigo = 1
    for produto in produtos:
        print("produto {}: R$ {}".format(codigo,produto))
        codigo += 1
    print("Total: R$ {}".format(round(TotalPagar,2)))
    print("Dinheiro: {}".format(round(Troco,2)))
    print("Troco: R$ {}".format(Troco-TotalPagar))
    print("-------------------------------------------------")



if __name__ == '__main__':
    print("Lojas Tabajara")   
    produto = []
    Quantidade = 1
    Total = float()
    Ancora =  True
    while(Ancora==True):
        print("QUANTIDADE PRODUTO:{}".format(Quantidade))
        Entrada = float(input("PREÇO "))
        Total += Entrada
        produto.append(Entrada)
        Quantidade += 1
        if(Entrada ==0.0):
            TotalDinhrito = float(input("Valor pago: "))
            Ancora = False

    NotaFiscal(produto,Total,TotalDinhrito)


