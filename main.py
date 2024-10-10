##############################################################
from random import seed
from random import choice, sample, randint
from restaurante import Restaurante
from personas import Cocinero, Repartidor, Cliente
## Si necesita agregar imports, debe agregarlos aquí arriba ##


### INICIO PARTE 4 ###

def crear_repartidores():
    repartidores = [Repartidor(choice(NOMBRES)) for _ in range(2)]
    return repartidores

def crear_cocineros():
    cocineros = [Cocinero(choice(NOMBRES), randint(1, 10)) for _ in range(5)]
    return cocineros

def crear_clientes():
    clientes = []
    for _ in range(5):
        nombre_cliente = choice(NOMBRES)
        platos_preferidos = sample(list(INFO_PLATOS.keys()), randint(1, 5))
        clientes.append(Cliente(nombre_cliente, platos_preferidos))
    return clientes

def crear_restaurante():
    cocineros = crear_cocineros()
    repartidores = crear_repartidores()
    restaurante = Restaurante("El Buen Comer", INFO_PLATOS, cocineros, repartidores)
    return restaurante


### FIN PARTE 4 ###

################################################################
## No debe modificar nada de abajo en este archivo.
## Este archivo debe ser ejecutado para probar el funcionamiento
## de su programa orientado a objetos.
################################################################




INFO_PLATOS = {
    "Pepsi": ["Pepsi", "Bebestible"],
    "Coca-Cola": ["Coca-Cola", "Bebestible"],
    "Jugo Natural": ["Jugo Natural", "Bebestible"],
    "Agua": ["Agua", "Bebestible"],
    "Papas Duqueza": ["Papas Duqueza", "Comestible"],
    "Lomo a lo Pobre": ["Lomo a lo Pobre", "Comestible"],
    "Empanadas": ["Empanadas", "Comestible"],
    "Mariscos": ["Mariscos", "Comestible"],
}

NOMBRES = ["Cristian", "Antonio", "Francisca", "Juan", "Jorge", "Pablo", "Luis", "Sofia", "Macarena"]

if __name__ == "__main__":

    ### Código para probar que tu miniproyecto esté funcionando correctamente  ###
    ### Corre directamente este archivo para que este código se ejecute ###
    #seed("DSP")
    seed("nuevaDePrueba")
    restaurante = crear_restaurante() # Crea el restaurante a partir de la función crear_restaurante()
    clientes = crear_clientes() # Crea los clientes a partir de la función crear_clientes()
    if restaurante != None and clientes != None:
        restaurante.recibir_pedidos(clientes) # Corre el método recibir_pedidos(clientes) para actualizar la calificación del restaurante
        print(
            f"La calificación final del restaurante {restaurante.nombre} "
            f"es {restaurante.calificacion}"
        )
    elif restaurante == None:
        print("la funcion crear_restaurante() no esta retornando la instancia del restaurante")
    elif clientes == None:
        print("la funcion crear_clientes() no esta retornando la instancia de los clientes")

