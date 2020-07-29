# -*- coding: utf-8 -*-

#Recode into new variables in python
start_list = [5, 3, 1, 2, 4]
square_list = [] #new variable

for number in start_list:
    number = number ** 2
    square_list.append(number)

square_list.sort()

print square_list


#multiplicacao de lista por valor. Ainda nao sei multiplicar cada valor entre duas listas.
my_list = [1,9,3,8,5,7]
my_list_weight = []

for number in my_list:
    number= number * 2
    my_list_weight.append(number)
print my_list_weight
    
#creating dictionaries/ recode variables
residents = {'Puffin' : 104, 'Sloth' : 105, 'Burmese Python' : 106}

#Recode UF PNAD - Codigo Lincoln
REGIOES_TABLE = {
    'norte':        [11, 12, 13, 14, 15, 16, 17],
    'nordeste':     [21, 22, 23, 24, 25, 26, 27, 28, 29],
    'sul':          [41,42, 43],
    'centro-oeste': [50, 51, 52, 53],
    'sp':           [35],
    'rj':           [33],
    'mg':           [31],
    'es':           [32],
    'brasil':       [88],
    'estrangeiro':  [98],
}

#One more example - dictonary
webster = {
	"Aardvark" : "A star of a popular children's cartoon show.",
    "Baa" : "The sound a goat makes.",
    "Carpet": "Goes on the floor.",
    "Dab": "A small amount."
}

# Add your code below!
for key in webster:
    print key, '.....', webster[key]
#    print webster[key]