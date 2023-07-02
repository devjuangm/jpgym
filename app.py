# CONTROL DE MEMBRESIAS EN EL GIMNASIO JP SCHWARZENEGGER

# VARIABLES
membresias = {
    "Juan": "Premium",
    "Fabio": "Básica",
    "Messi": "Premium",
    "Janeth": "Básica",
    "James": "Premium"
}

# OPERADORES
costo_premium = 100
costo_basica = 50

print("¡Bienvenido al gimnasio bro!")

# LISTAS
clientes_premium = []
clientes_basica = []

# TUPLAS
horarios = ("Mañana", "Tarde", "Noche")

# SETS
actividades = {"Yoga", "Spinning", "Zumba", "CrossFit"}

# DICCIONARIOS
precios_actividades = {
    "Yoga": 10,
    "Spinning": 15,
    "Zumba": 20,
    "CrossFit": 25
}

# USO DE CONDICIONALES (IF, ELIF)
def calcular_costo_membresia(cliente):
    if membresias[cliente] == "Premium":
        return costo_premium
    elif membresias[cliente] == "Básica":
        return costo_basica

cliente_elegido = input("Ingrese el nombre del cliente: ")

if cliente_elegido in membresias:
    costo_membresia = calcular_costo_membresia(cliente_elegido)
    print(f"El costo de la membresía de {cliente_elegido} es: ${costo_membresia}")
else:
    print("El cliente ingresado no existe en el sistema.")

# USO DE BUCLES, AGREGAMOS LOS CLIENTES A LAS LISTAS SEGUN SU MEMBRESIA
for cliente, tipo_membresia in membresias.items():
    if tipo_membresia == "Premium":
        clientes_premium.append(cliente)
    elif tipo_membresia == "Básica":
        clientes_basica.append(cliente)

# Funciones, SE CALCULA EL COSTO TOTAL
def calcular_costo_actividades(actividades_elegidas):
    costo_total = 0
    for actividad in actividades_elegidas:
        costo_total += precios_actividades[actividad]
    return costo_total

#ESTE ES EL USO DE LAS FUNCIONES Y CONDICIONALES, NOS PEDIRA EL NOMBRE Y DARA LOS DATOS RECOLECTADOS
actividades_elegidas = ["Yoga", "Spinning", "CrossFit"]
costo_actividades = calcular_costo_actividades(actividades_elegidas)

if cliente_elegido in membresias:
    actividades_elegidas = ["Yoga", "Spinning", "CrossFit"]
    costo_actividades = calcular_costo_actividades(actividades_elegidas)
    print(f"El costo total de las actividades elegidas es: ${costo_actividades}")
else:
    print("No existe ningún valor en actividades elegidas")