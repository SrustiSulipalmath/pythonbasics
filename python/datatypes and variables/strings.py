print("giraffe\nacademy") #insert new line  backslash n
print("giraffe\"academy")
print("giraffe\\academy")

phrase = "giraffe academy"
print(phrase)

#concatination appending one string to another
print(phrase +" is cool")

#functions
print(phrase.lower())
print(phrase.upper())
print(phrase.isupper())
print(phrase.islower())
print(phrase.upper().isupper())
print(len(phrase)) #number of characters
print(phrase[0])  #individual characters  specific character
print(phrase.index("g"))
print(phrase.index("acad"))
print(phrase.replace("giraffe","elephant"))