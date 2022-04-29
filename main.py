import time

# Este es un programa que a partir del peso en la tierra de un cuerpo, devuelve
# el peso de ese mismo cuerpo en otro astro del sistema solar

# Diccionario con las aceleraciones de la gravedad en otros planetas
aceleracion_gravedad = {'mercurio': 3.7, 'venus': 8.87, 'tierra': 9.81,
                        'luna': 1.62, 'marte': 3.711, 'júpiter': 24.79,
                        'saturno': 10.44, 'urano': 8.69, 'neptuno': 11.15}


# La función recibe como parámetros la masa del cuerpo,
# el astro en el que queremos averiguar el peso y el diccionario
# con las aceleraciones gravitatorias.
# El diccionario con las aceleraciones se pasa por defecto
# la función devuelve el resultado de multipicar la masa por la división entre
# gravedad en el astro por la gravedad en la tierra.
# Si no se especifica el planeta se sobre entiende que es la tierra.
def peso_relativo(masa, planeta='tierra',
                  dicc_aceleraciones=aceleracion_gravedad):
    planeta = planeta.lower()  # El argumento se pasa a minúsculas
    planeta = planeta.strip()  # Se eliminan los espacios
    return masa * dicc_aceleraciones[planeta]


masa = float(input('Introduzca la masa del cuerpo (en kg)> '))
# Creamos una lista con los planetas a partir del diccionario
planeta = input('introduzca el un planeta del sistema solar> ')
# convertimos el nombre del planeta a minúsculas
planeta = planeta.lower()
# eliminamos los espacios en blanco
planeta = planeta.strip()

# guardamos la fecha con una precisión de segundos para dar 
# así un nombre único a nuestro fichero
timestr = time.strftime("%y%m%d-%H%M%S")

with open(f'peso_{timestr}.txt', 'w') as f:
    output = f"Un cuerpo de {masa} kg pesa {peso_relativo(masa, planeta):.2f} newtons en el planeta {planeta}."
    f.write(output)
