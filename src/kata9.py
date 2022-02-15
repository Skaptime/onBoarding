#Exercise 1: work with arguments in fuctions
def tankReport(tank1, tank2, tank3):
    average = (tank1 + tank2 + tank3) / 3
    return f"""Reporte de tanques:
    Promedio total: {average}%
    Tanque 1: {tank1}%
    Tanque 2: {tank2}%
    Tanque 3: {tank3}% 
    """

print(tankReport(40, 50, 60))

def average(values):
    total = sum(values)
    items = len(values)
    return total / items

average([70, 80, 90]) 

def report(tank1, tank2, tank3):
    return f"""Reporte de tanques:
    Promedio: {average([tank1, tank2, tank3])}%
    Tanque 1: {tank1}%
    Tanque 2: {tank2}%
    tanque 3: {tank3}% 
    """

# Call the updated function again with different values
print(report(88, 76, 70))


#-----------------------------------------------
#-----------------------------------------------
#Exercise 2: Work with key words of arguments

def missionReport(launchTime, destination, flight, tank1, tank2, tank3):
    return f"""
    Destino {destination}
    Tiempo de viaje: {launchTime + flight} mn
    Combistible disponible: {tank1 + tank2 + tank3} litros
    """

print(missionReport(5, "Luna", 562, 200000, 300000, 130000))

#------------------------------New function ------------------------

def missionReport(destination, *minutes, **fuel_reservoirs):
    main_report = f"""
    Mission to {destination}
    Total travel time: {sum(minutes)} minutes
    Total fuel left: {sum(fuel_reservoirs.values())}
    """
    for tank_name, gallons in fuel_reservoirs.items():
        main_report += f"{tank_name} tank --> {gallons} gallons left\n"
    return main_report

print(missionReport("Moon", 8, 11, 55, main=300000, external=200000))