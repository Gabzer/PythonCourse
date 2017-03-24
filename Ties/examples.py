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