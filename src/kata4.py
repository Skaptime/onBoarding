#Exercice 1: change the string

text = """Interesting facts about the Moon. The Moon is Earth's only satellite. There are several interesting facts about the Moon and how it affects life here on Earth. 
On average, the Moon moves 4cm away from the Earth every year. This yearly drift is not significant enough to cause immediate effects on Earth. The highest daylight temperature of the Moon is 127 C."""
# Split the text in each sentence to work o it.
str = text.split('.')
str

#Declare some key words to search and helped you to determinate if one sentence contains a fact
keyWords = ["average", "temperature", "distance"]

#Create a bucle and print just moon data that are related whit the key word previously defined
for sentence in str:
    for keyword in keyWords:
        if keyword in sentence:
            print(sentence)
            break

#Finally, update the bucle and change the C to Celsius 
for sentence in str:
    for keyWord in keyWords:
        if keyWord in sentence:
            print(sentence.replace(' C', 'Celsius'))
            break

#--------------------------------Exercise 2---------------------------
name = "Moon"
gravity = 0.00162 # in kms
planet = "Earth"

#First, Create a title for the text. this text is about the gravity in the earth an th moon 
#Use it to create a meaning title
title = f'Gravedad en {name}'

#now create a multiline string template to save the rest of the information, convert the 
#distance from kilometres to meters multiplied by 10000.
facts = f"""{'-'*80} 
Nombre: {planet} 
Gravedad: {gravity * 1000} m/s2 
"""

#Finally, use each sentences to join the title and the fact
template = f"""{title.title()} 
{facts} 
""" 
print(facts)
#---------------- New information------------------
planet = 'Marte '
gravity  = 0.00143
name = 'Ganímedes'


newT = """
Gravedad en: {nombre}
Nombre: {planeta}
Gravedad : {gravedad} m/s2
"""
print(newT.format(nombre=name, planeta=planet, gravedad=gravity*1000))