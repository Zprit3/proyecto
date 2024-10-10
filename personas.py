from random import randint
from platos import Comestible, Bebestible


### INICIO PARTE 2.1 ###
class Persona:
    def __init__(self, nombre):
        self.nombre = nombre


### FIN PARTE 2.1 ###

### INICIO PARTE 2.2 ###
class Repartidor(Persona):
    def __init__(self, nombre):
        super().__init__(nombre)
        self.tiempo_entrega = randint(20, 30)
        self.energia = randint(75, 100)

    def repartir(self, pedido):
        # Calculamos el factor tamaño y factor velocidad según el número de platos
        num_platos = len(pedido)

        if num_platos <= 2:
            factor_tamaño = 5
            factor_velocidad = 1.25
        else:
            factor_tamaño = 15
            factor_velocidad = 0.85

        # tiempo de demora
        tiempo_demorado = self.tiempo_entrega * factor_velocidad

        # Disminucion de tamaño
        self.energia -= factor_tamaño

        return tiempo_demorado


### FIN PARTE 2.2 ###

### INICIO PARTE 2.3 ###
class Cocinero(Persona):
    def __init__(self, nombre, habilidad):
        super().__init__(nombre)
        self.habilidad = habilidad
        self.energia = randint(50, 80)  # Inicialización de energía

    def cocinar(self, informacion_plato):
        nombre, tipo = informacion_plato

        if tipo == "Bebestible":
            plato = Bebestible(nombre)
            if plato.tamano == "Pequeño":
                self.energia -= 5
            elif plato.tamano == "Mediano":
                self.energia -= 8
            elif plato.tamano == "Grande":
                self.energia -= 10
        elif tipo == "Comestible":
            plato = Comestible(nombre)
            self.energia -= 15

        # Aca se ajusta la calidad según la dificultad y habilidad
        factor_calidad = 1.5 if plato.dificultad <= self.habilidad else 0.7
        plato.calidad *= factor_calidad

        return plato


### FIN PARTE 2.3 ###

### INICIO PARTE 2.4 ###
class Cliente(Persona):
    def __init__(self, nombre, platos_preferidos):
        super().__init__(nombre)
        self.platos_preferidos = platos_preferidos  # Espera una lista de nombres de platos

    def recibir_pedido(self, pedido, demora):
        calificacion = 10  # Inicializa la calificación en 10

        # La condicion para dividir la calificación a la mitad

        if len(pedido) < len(self.platos_preferidos) or demora >= 20:
            calificacion /= 2

        # Se evalua la calidad de cada plato en el pedido
        for plato in pedido:
            calidad = plato.calidad  # Asumiendo que cada plato tiene un atributo `calidad`

            if calidad >= 11:
                calificacion += 1.5
            elif calidad <= 8:
                calificacion -= 3
                # Asegurarse de que la calificación no baje de 0
                if calificacion < 0:
                    calificacion = 0

        return calificacion  # Retorna la calificación final


### FIN PARTE 2.4 ###

if __name__ == "__main__":
    ### Código para probar que tu clase haya sido creada correctamente  ###
    ### Corre directamente este archivo para que este código se ejecute ###
    try:
        # Creamos algunos platos de prueba
        PLATOS_PRUEBA = [
            Bebestible("Coca-Cola"),
            Bebestible("Jugo Natural"),
            Comestible("Sopa"),
            Comestible("Empanadas"),
            Bebestible("Agua"),
            Comestible("Pizza"),
        ]

        # Creamos una instancia de cada clase
        un_cocinero = Cocinero("Cristian", randint(1, 10))
        un_repartidor = Repartidor("Tomás")
        platos_preferidos = ["Coca-Cola", "Sopa", "Pizza"]  # Nombres de los platos preferidos
        un_cliente = Cliente("Alberto", platos_preferidos)

        print(
            f"El cocinero {un_cocinero.nombre} tiene una habilidad de: {un_cocinero.habilidad} y energía de: {un_cocinero.energia:.2f}")
        print(
            f"El repartidor {un_repartidor.nombre} tiene un tiempo de entrega de: {un_repartidor.tiempo_entrega:.2f} seg")

        # Simulamos el cocinar un plato
        plato_a_cocinar = ["Limonada", "Bebestible"]
        plato_cocinado = un_cocinero.cocinar(plato_a_cocinar)
        print(f"Plato cocinado: {plato_cocinado.nombre}, tipo: Bebestible, calidad: {plato_cocinado.calidad:.2f}")
        print(f"Energía restante del cocinero: {un_cocinero.energia:.2f}")

        # Simulamos el repartir un pedido
        pedido = [plato_cocinado, PLATOS_PRUEBA[2]]  # Incluyendo Limonada y Sopa
        tiempo_demorado = un_repartidor.repartir(pedido)
        print(f"Tiempo de demora en la entrega: {tiempo_demorado:.2f} seg")
        print(f"Energía restante del repartidor: {un_repartidor.energia:.2f}")

        # PRUEBAS ESPECÍFICAS PARA CLASE CLIENTE:

        # Simular recibir un pedido con platos preferidos
        pedido_preferidos = [PLATOS_PRUEBA[0], PLATOS_PRUEBA[2], PLATOS_PRUEBA[5]]  # Incluyendo Coca-Cola, Sopa y Pizza
        calificacion_preferidos = un_cliente.recibir_pedido(pedido_preferidos, 15)  # Demora de 15
        print(f"Calificación del cliente (pedido preferidos): {calificacion_preferidos:.2f}")

        # Otro pedido con alta demora
        calificacion_demorada = un_cliente.recibir_pedido(pedido_preferidos, 25)  # Demora de 25
        print(f"Calificación del cliente con alta demora: {calificacion_demorada:.2f}")

        # Simular recibir un pedido con menos platos que los preferidos
        pedido_menor = [PLATOS_PRUEBA[0]]  # Solo Coca-Cola
        calificacion_menor = un_cliente.recibir_pedido(pedido_menor, 15)  # Demora de 15
        print(f"Calificación del cliente (pedido menor): {calificacion_menor:.2f}")

    except ValueError as e:
        print(e)

    except TypeError:
        print("Hay una cantidad incorrecta de argumentos en algún inicializador y/o todavía no defines una clase")
    except AttributeError:
        print("Algún atributo está mal definido y/o todavía no defines una clase")
