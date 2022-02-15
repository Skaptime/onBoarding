#Exercise 1: create a python dictionary
planet = {
    'name': 'Mars',
    'moons': 2
}
print("Planeta: ",planet.get('name')," y tiene ", planet.get('moons')," lunas")
#///-----------------add the circumference
planet['circunferencia(km)'] = {
    'polar': 6752,
    'equatorial': 6792
}
print(f'{planet.get("name")} has a polar circumference of {planet["circunferencia(km)"]["polar"]}')
#Excercise 2: dynamic programming using a dictionary 
planet_moons = {
    'mercury': 0,
    'venus': 0,
    'earth': 1,
    'mars': 2,
    'jupiter': 79,
    'saturn': 82,
    'uranus': 27,
    'neptune': 14,
    'pluto': 5,
    'haumea': 2,
    'makemake': 1,
    'eris': 1
}
moons = planet_moons.values()
planets = len(planet_moons.keys())

total_moons = 0
for moon in moons:
    total_moons = total_moons + moon

print("El promedio de lunas es:",total_moons / planets)