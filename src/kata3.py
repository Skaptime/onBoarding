#Para este ejercicio, escribirás una lógica condicional que imprima una advertencia si un 
#asteroide se acerca a la Tierra demasiado rápido. La velocidad del asteroide varía
#dependiendo de lo cerca que esté del sol, y cualquier velocidad superior a 25 kilómetros
#por segundo (km/s) merece una advertencia.
#Un asteroide se acerca, y viaja a una velocidad de 49 km/s.

velocidad = 49

if velocidad > 25:
    print("Alerta por el asteroide")
else:
    print("No hay porque alertarse")

# Agrega el código para crear una variable para un asteroide que viaja a 19 km/s
# Escribe varias expresiones de prueba para determinar si puedes ver el rayo de luz desde la tierra
# Agrega las instrucciones que se ejecutarán si las expresiones de prueba son True o False
asteroide = 19
if asteroide > 20:
    print("Hay uno que se dirige a la tierra ahora a una velocidad mayor a 20 km/s")
elif asteroide ==20:
    print("Hay uno que se dirige a la tierra ahora a una velocidad de 20 km/s")
else:
    print("No hay de que alertarse")

# Agrega el código para crear nuevas variables para la velocidad y el tamaño del asteroide
# Para probar el código, prueba con varias velocidades y tamaños
# Escribe varias expresiones de prueba o combinaciones de expresiones de prueba para determinar qué mensaje se debe enviar a Tierra.

speed = 20
size = 188

if speed > 25 and size > 25:
    print('Alerta de asteroide peligroso a más de 25 km/hr')
elif speed >= 20:
    print("En el cielo se puede ver una luz")
elif size < 25:
    print("No hay peligro")
else:
    print("No hay peligro")