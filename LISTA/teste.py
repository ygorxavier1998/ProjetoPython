'''
athletes = [['Phelps', 'Lochte', 'Schooling', 'Ledecky', 'Franklin'], ['Felix', 'Bolt', 'Gardner', 'Eaton'], ['Biles', 'Douglas', 'Hamm', 'Raisman', 'Mikulak', 'Dalton']]
other = []
for Lista in athletes:
    for item in Lista:
        if('t' in item):
            other.append(item)
print(item)

liste =  ["1","2","3","4"]
liste1 = ["5","6","7","8"]


liste3 = list(zip(liste,liste1))
print(liste3)


lst_check = ['plums', 'watermelon', 'kiwi', 'strawberries', 'blueberries', 'peaches', 'apples', 'mangos', 'papaya']
map_testing = list(map(lambda fruta: "Fruit: "+fruta, lst_check))
print(map_testing)




countries = ['Canada', 'Mexico', 'Brazil', 'Chile', 'Denmark', 'Botswana', 'Spain', 'Britain', 'Portugal', 'Russia', 'Thailand', 'Bangladesh', 'Nigeria', 'Argentina', 'Belarus', 'Laos', 'Australia', 'Panama', 'Egypt', 'Morocco', 'Switzerland', 'Belgium']
b_countries = []


def respc(tr):
    for Pais in tr:
        if(Pais[0]=='B'):
            return True
        else:
            return False
        
b_countries = list(filter(respc,countries))

print(b_countries)



people = [('Snow', 'Jon'), ('Lannister', 'Cersei'), ('Stark', 'Arya'), ('Stark', 'Robb'), ('Lannister', 'Jamie'), ('Targaryen', 'Daenerys'), ('Stark', 'Sansa'), ('Tyrell', 'Margaery'), ('Stark', 'Eddard'), ('Lannister', 'Tyrion'), ('Baratheon', 'Joffrey'), ('Bolton', 'Ramsey'), ('Baelish', 'Peter')]
first_names = []

firt , first_names = zip(*people)

print(list(first_names))

lst = [["hi", "bye"], "hello", "goodbye", [9, 2], 4]

lst1 = map(lambda item: item+item,lst)
print(list(lst1))



students = [('Tommy', 95), ('Linda', 63), ('Carl', 70), ('Bob', 100), ('Raymond', 50), ('Sue', 75)]

passed = list(filter(lambda x: x[1] >= 70,students))

passed = [nome[0] for nome in passed]
print(passed)
'''

#REST APIS
##API, it's an acronym that stands for Application Programming Interface.

#url - 

#https://www.coursera.org/learn/data-collection-processing-python/lecture/94uZH/urls-domain-names-and-ip-addresses
######|
#PROTOCAL
##HOST SERVER --->NOME DE UM COMPUTADOR QUE NOS COMUNICAMOS
##Domain Name - Dominio nome especifico de um site
##IP Addresses - identificação unica de um computador
##Routing -->O roteamento de redes é o processo de seleção de um caminho em uma ou mais redes.
##


import json

import requests as req

'''
pagina = req.get("https://api.datamuse.com/words?rel_rhy=funny")
print(pagina.text[:150])
print(pagina.url)
print("---------------------")

x = pagina.json()
print(x[0])

print(json.dumps(x,indent=2))

key_pais={'rel_rhy':'funny'}
pagina = req.get("https://api.datamuse.com/words",params=key_pais)
print(pagina.text[:150])
print(pagina.url)


d={'q':'elefante'}
resultado = req.get("https://www.google.com/", params=d)
print(resultado)
print(resultado.url)

import requests_with_caching
# it's not found in the permanent cache
res = requests_with_caching.get("https://api.datamuse.com/words?rel_rhy=happy", permanent_cache_file="datamuse_cache.txt")
print(res.text[:100])
# this time it will be found in the temporary cache
res = requests_with_caching.get("https://api.datamuse.com/words?rel_rhy=happy", permanent_cache_file="datamuse_cache.txt")
# This one is in the permanent cache.
res = requests_with_caching.get("https://api.datamuse.com/words?rel_rhy=funny", permanent_cache_file="datamuse_cache.txt")

https://itunes.apple.com/search?parameterkeyvalue
'''

parameters = {"term": "j-cole"}
iTunes_response = req.get("https://itunes.apple.com/search", params = parameters)

print(iTunes_response.text[:500])