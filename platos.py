import random
from enum import Enum

class TamanoBebestible(Enum):
    PEQUENO = "Pequeño"
    MEDIANO = "Mediano"
    GRANDE = "Grande"


### INICIO PARTE 1.1 ###
class Plato:
    def __init__(self, nombre):
        self.nombre = nombre
        self.calidad = 0
### FIN PARTE 1.1 ###

### INICIO PARTE 1.2 ###
class Bebestible(Plato):
    def __init__(self, nombre):
        super().__init__(nombre)

        self.tamano = random.choice(list(TamanoBebestible)).value

        if self.tamano == TamanoBebestible.PEQUENO.value:
            self.dificultad = 3
        elif self.tamano == TamanoBebestible.MEDIANO.value:
            self.dificultad = 6
        elif self.tamano == TamanoBebestible.GRANDE.value:
            self.dificultad = 9

        self.calidad = random.randint(3, 8)
### FIN PARTE 1.2 ###

### INICIO PARTE 1.3 ###
class Comestible(Plato):
    def __init__(self, nombre):
        super().__init__(nombre)
        self.dificultad = random.randint(1, 10)
        self.calidad = random.randint(5, 10)
### FIN PARTE 1.3 ###


if __name__ == "__main__":
    ### Código para probar que tu clase haya sido creada correctamente  ###
    ### Corre directamente este archivo para que este código se ejecute ###
    try:
        un_bebestible = Bebestible("Coca-Cola")
        un_comestible = Comestible("Sopa")
        print(f"Esto es una {un_bebestible.nombre} de tamaño {un_bebestible.tamano} y calidad {un_bebestible.calidad}.")
        print(f"Esto es una {un_comestible.nombre} de dificultad {un_comestible.dificultad} y calidad {un_comestible.calidad}.")
    except TypeError:
        print("Hay una cantidad incorrecta de argumentos en algún inicializador y/o todavía no defines una clase")
    except AttributeError:
        print("Algún atributo esta mal definido y/o todavia no defines una clase")
