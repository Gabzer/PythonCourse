######################################################################
suitcase = [] 
suitcase.append("oculos escuros")
suitcase.append("bermuda")
suitcase.append("chinelo")
suitcase.append("boné")

list_length = len(suitcase) # Iguale ao comprimento da valise

print "Ha %d itens na valise." % (list_length)
print suitcase
######################################################################
animals = ["tatu", "texugo", "pato", "emu", "raposa"]
duck_index = animals.index("pato")  # Use index() para encontrar "pato"

animals.insert(duck_index, "cobra")

print animals
######################################################################
######--FOR
my_list = [1,9,3,8,5,7]

for number in my_list:
    # Seu codigo aqui
    print 2 * number
######################################################################
######--.append() e .sort()
start_list = [5, 3, 1, 2, 4]
square_list = []

for number in start_list:
    square_list.append(number ** 2)
square_list.sort()
print square_list
######################################################################
# key - animal_name : value - location 
zoo_animals = { 'Unicornio' : 'Casa de Algodao Doce',
'Preguica' : 'Exibicao da Floresta Tropical',
'Tigre de Bengala' : 'Casa da Selva',
'Fradinho do Atlantico' : 'Exibicao Artica',
'Pinguim Saltador da Rocha' : 'Exibicao Artica'}
# Uma declaracao de dicionario (ou lista) pode ocupar mais de uma linha

# Removendo a entrada 'Unicornio'( Unicornios sao incrivelmente caros).
del zoo_animals['Unicornio']
del zoo_animals['Preguica']
del zoo_animals['Tigre de Bengala']
zoo_animals['Pinguim Saltador da Rocha'] = 'Coiso'

print zoo_animals
######################################################################
backpack = ['xilofone', 'adaga', 'tenda', 'pedaco de pao']
backpack.remove('adaga')
######################################################################
inventory = {
    'gold' : 500,
    'pouch' : ['silex', 'barbante', 'pedra preciosa'], # Atribuido uma nova lista a chave 'pouch'
    'backpack' : ['xilofone','adaga', 'saco de dormir','pedaco de pao']
}
# Adicionando uma chave 'burlap bag' a atribuindo uma lista a ela
inventory['burlap bag'] = ['maca', 'pequeno rubi', 'bicho preguica']
# Organizando a lista encontrada sob a chave 'pouch'
inventory['pouch'].sort() 

inventory['pocket'] = ['concha', 'amora estranha', 'sujeira']
inventory['backpack'].sort() 
inventory['backpack'].remove('adaga')
inventory['gold'] += 50