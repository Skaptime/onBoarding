#Exercise 1 math operators:  calculate the distance between two planets

earth = 149597870
jupiter = 778547200

distance = earth-jupiter
print(abs(distance))

miles = distance * 0.621
print(miles)
#------------------------ new values--------------
print("-------------------New values---------------------------------- ")
earth = 628949330
jupiter = 390577534
distance = earth-jupiter
print(abs(distance))

miles = distance * 0.621
print(miles)

#Exercise 2 convert Strings to numbers usig absolute values 
number1 = input("¿Cuál es el primer número?")
planet1 = int(number1)
number2 = input("¿Cúál es el segundo número?")
planet2 = int(number2)
print("La distancia es de: "+str(planet1-planet2))
print("Con valor absoluto es: "+str(abs(planet1-planet2)))