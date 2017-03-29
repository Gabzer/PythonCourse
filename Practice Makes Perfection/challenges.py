#challenge 1
def is_even(x):
    if x % 2 == 0:
        return True
    else:
        return False

#challenge 2
def is_int(x):
    if int(x) - x == 0:
        return True
    else:
        return False

#challenge 3: sum of a string
def digit_sum(n):
    digits = [int(d) for d in str(n)]
    b = sum(digits)
    return(b)

#challenge 4: make a factorial number
def factorial(x):
    total = 1
    while x > 0:
        total = total * x
        x -= 1
    return total

#challenge 5: prime numbers
def is_prime(x):
    isPrime = False
    if (x < 2):
       isPrime = False
    elif (x == 2):
        isPrime = True
    else:
        for n in range(2,x):
            if ( x % n) == 0:
                isPrime = False
                break
            else:
                isPrime = True
    return isPrime

#challenge 6: reverse string
def reverse(text):
    x = len(text) - 1
    rever = ""
    while x >= 0:
        rever = rever + text[x]
        x -= 1
    return rever

#challenge 7: not vowel
def anti_vowel(text):
    string = ""
    for n in text:
        if n not in "aeiouAEIOU":
            string = string + n
    return string

#challenge 8: scrabble
score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2, 
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3, 
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1, 
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4, 
         "x": 8, "z": 10}

def scrabble_score(word):
    total = 0
    for n in word.lower():
        for x in score:
            if n == x:
                total = total + score[x]
    return total

#challenge 9:
def censor (text, word):
    a = "*" * len(word)
    text = text.split(" ")
    for i in range(len(text)):
        if word == text[i]:
            text[i] = a
    return " ".join(text)

#challenge 10:
def count(sequence, item):
    count = 0
    for x in sequence:
        if x == item:
            count += 1
    return count

#challenge 11: purify the list
def purify(list):
    pars = []
    for x in list:
        if x % 2 == 0:
            pars.append(x)
    return pars

#challenge 12: product
def product(list):
    total = 1
    for x in list:
        total = total * x
    return total

#challenge 13:
def remove_duplicates(list):
    duplic = []
    x = len(list)
    range_ = range(x)
    for n in range_:
        if not list[n] in list[n+1:]:
            duplic.append(list[n])
    return duplic