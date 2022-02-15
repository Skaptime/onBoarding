#Exercise 1: create and use a list 
planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Neptune']
print("Los planetas son:",len(planets), planets)
#Add plutón
planets.append("Plutón")

print(planets[-1], "Es el último planeta")

#Exercise 2:Working with a data list
planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Neptune']
name = input("Ingresa el nombre de un planeta ")
planet = planets.index(name)
#-----------------show the plantes who are near from sun
print("Los planetas más cercanos al sol que ", name," son: ")
print(planets[0:planet])

#-----------------show the plantes who are far from sun
print("Los planetas más lejanos al sol que ", name," son: ")
print(planets[planet+1:len(planets)])
