#Exercise 1:create a while bucle
nPlanet = ''
planets = []

while nPlanet.lower() != "hecho":
    if nPlanet:
        planets.append(nPlanet)
    nPlanet = input("Ingresa un nuevo planeta")

#Exercise 2: Create a for bucle

for namePlanet in planets:
    print(namePlanet)
