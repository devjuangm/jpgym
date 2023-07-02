# # CONTROL DE MEMBRESIAS EN EL GIMNASIO JP SCHWARZENEGGER

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

# print("¡Bienvenido al gimnasio bro!")

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

# cliente_elegido = input("Ingrese el nombre del cliente: ")

# if cliente_elegido in membresias:
#     costo_membresia = calcular_costo_membresia(cliente_elegido)
#     print(f"El costo de la membresía de {cliente_elegido} es: ${costo_membresia}")
# else:
#     print("El cliente ingresado no existe en el sistema.")

# # USO DE BUCLES, AGREGAMOS LOS CLIENTES A LAS LISTAS SEGUN SU MEMBRESIA
# for cliente, tipo_membresia in membresias.items():
#     if tipo_membresia == "Premium":
#         clientes_premium.append(cliente)
#     elif tipo_membresia == "Básica":
#         clientes_basica.append(cliente)

# Funciones, SE CALCULA EL COSTO TOTAL
def calcular_costo_actividades(actividades_elegidas):
    costo_total = precios_actividades[actividades_elegidas]
    # costo_total = 0
    # for actividad in actividades_elegidas:
    #     costo_total += precios_actividades[actividad]
    return costo_total

# #ESTE ES EL USO DE LAS FUNCIONES Y CONDICIONALES, NOS PEDIRA EL NOMBRE Y DARA LOS DATOS RECOLECTADOS
# actividades_elegidas = ["Yoga", "Spinning", "CrossFit"]
# costo_actividades = calcular_costo_actividades(actividades_elegidas)

# if cliente_elegido in membresias:
#     actividades_elegidas = ["Yoga", "Spinning", "CrossFit"]
#     costo_actividades = calcular_costo_actividades(actividades_elegidas)
#     print(f"El costo total de las actividades elegidas es: ${costo_actividades}")
# else:
#     print("No existe ningún valor en actividades elegidas")




import streamlit as st

def main():
    st.title("GIMNASIO JP SCHWARZENEGGER")
    
    # Seccion del usuario y el costo de la membresia
    nombre_usuario = st.selectbox("Seleccione el nombre del usuario", membresias)
    costo_calculado = calcular_costo_membresia(nombre_usuario)
    st.info(f"El costo calculado para el usuario es de: ${costo_calculado}")
    
    # Seccion de las actividades
    nombre_actividad = st.selectbox("Seleccione el nombre de la actividad", precios_actividades)
    costo_actividad_calculado = calcular_costo_actividades(nombre_actividad)
    st.info(f"El costo calculado para la actividad es de: ${costo_actividad_calculado}")
    pic = st.camera_input("Take a picture")
    numero = st.slider('Pick a number', 0, 100)
    st.multiselect('Buy', ['milk', 'apples', 'potatoes'])
    st.radio('Pick one', ['cats', 'dogs'])
    st.checkbox('I agree')
    st.button('Click me')
    
    tab1, tab2 = st.tabs(["Tab 1", "Tab2"])
    tab1.write("this is tab 1")
    tab1.image('img/img1.webp', width=80)
    tab2.write("this is tab 2")
    tab2.metric('My metric', 42, 2)
    
    st.error('Error message')
    st.warning('Warning message')
    st.info('Info message')
    st.success('Success message')
    st.snow()
    st.balloons()
    st.progress(80)




    
if __name__ == '__main__':
    main()

    