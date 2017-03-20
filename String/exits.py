#transform into string
pi = 3.14
print str(pi)

#Convert to string is required in a sentence
print "O valor de pi e' de cerca de " + str(3.14)

#Formatting Strings with %
name = raw_input("Qual e o seu nome?")
quest = raw_input("Qual e sua missao?")
color = raw_input("Qual e sua cor favorita?")

print "Ah, entao seu nome e %s, sua missao e %s, " \
"e sua cor favorita e %s." % (name, quest, color)