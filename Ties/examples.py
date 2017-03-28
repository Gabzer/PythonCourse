choice = raw_input('Gostando do curso? (y/n)')

while choice != 'y' and choice != 'n':
    choice = raw_input("Desculpe, nao entendi. Digite novamente: ")

############################################################
import random

print "Numeros da Sorte! Serao gerados 3 numeros."
print "Se um deles for um '5', voce perde!"

count = 0
while count < 3:
    num = random.randint(1, 6)
    print num
    if num == 5:
        print "Lamento, voce perdeu!"
        break
    count += 1
else:
    print "Voce ganhou!"
############################################################
from random import randint

# Gera um numero de 1 a 10, inclusive
random_number = randint(1, 10)

guesses_left = 3
# Comece seu jogo!
while guesses_left > 0:
    guess = int(raw_input("Seu palpite: "))
    if guess == random_number:
        print 'Voce venceu!'
        break
    guesses_left -= 1
else:
    print 'Voce perdeu.'
############################################################
phrase = "Um passaro na mao..."

# Adicione seu laco for
for char in phrase:
    if char == 'a' or char == 'A':
        print 'X',          #the , makes print on the same line
    else:
        print char,

choices = ['pizza', 'massa', 'salada', 'nachos']
############################################################
#ENUMERATE fornece um índice correspondente a cada elemento na lista que você está percorrendo
print 'Suas opcoes sao:'
for index, item in enumerate(choices):
    print index + 1, item
############################################################
#ZIP cria pares de elementos quando são usadas duas ou mais listas, e para no fim da lista mais curta
list_a = [3, 9, 17, 15, 19]
list_b = [2, 4, 8, 10, 30, 40, 50, 60, 70, 80, 90]

for a, b in zip(list_a, list_b):
    if a > b:
        print a
    else:
        print b
############################################################