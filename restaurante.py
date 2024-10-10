from random import randint

from personas import Cliente, Repartidor, Cocinero


### INICIO PARTE 3 ###
class Restaurante:
    def __init__(self, nombre, platos, cocineros, repartidores):
        self.nombre = nombre
        self.platos = platos
        self.cocineros = cocineros
        self.repartidores = repartidores
        self.calificacion = 0

    def recibir_pedidos(self, clientes):
        total_calificacion = 0

        for cliente in clientes:
            pedido = []  # Lista para acumular los platos cocinados
            for plato_nombre in cliente.platos_preferidos:
                # aca se verifica si el plato está en el menú del restaurante
                if plato_nombre in self.platos:
                    plato_info = self.platos[plato_nombre]
                    plato_tipo = plato_info[1]

                    # se selecciona un cocinero con energía positiva
                    cocinero = next((c for c in self.cocineros if c.energia > 0), None)
                    if cocinero:
                        plato_cocinado = cocinero.cocinar([plato_nombre, plato_tipo])
                        pedido.append(plato_cocinado)

            # repartidor con energia positiva
            repartidor = next((r for r in self.repartidores if r.energia > 0), None)
            if repartidor:
                demora = repartidor.repartir(pedido)
            else:
                # Si no hay repartidor disponible, demora es 0 y el pedido es vacío
                demora = 0
                pedido = []

            # El cliente recibe el pedido y la demora
            calificacion_cliente = cliente.recibir_pedido(pedido, demora)
            total_calificacion += calificacion_cliente

        # Actualizamos la calificación del restaurante
        if len(clientes) > 0:
            self.calificacion = total_calificacion / len(clientes)


### FIN PARTE 3 #


if __name__ == "__main__":
    ### Código para probar que tu clase haya sido creada correctamente  ###
    ### Corre directamente este archivo para que este código se ejecute ###
    try:
        # Creamos algunos platos de prueba
        PLATOS_PRUEBA = {
            "Coca-Cola": ["Coca-Cola", "Bebestible"],
            "Jugo Natural": ["Jugo Natural", "Bebestible"],
            "Sopa": ["Sopa", "Comestible"],
            "Empanadas": ["Empanadas", "Comestible"],
            "Agua": ["Agua", "Bebestible"],
            "Pizza": ["Pizza", "Comestible"],
        }

        # cocineros y repartidores de prueba
        cocineros_prueba = [Cocinero("Cristian", randint(1, 10)) for _ in range(3)]
        repartidores_prueba = [Repartidor("Tomás") for _ in range(2)]

        # algunos clientes de prueba
        clientes_prueba = [
            Cliente("Alberto", ["Coca-Cola", "Sopa", "Pizza"]),
            Cliente("Maria", ["Jugo Natural", "Empanadas"]),
            Cliente("Pedro", ["Agua", "Pizza"])
        ]

        # Creamos el restaurante
        restaurante_prueba = Restaurante("Restaurante Prueba", PLATOS_PRUEBA, cocineros_prueba, repartidores_prueba)

        # Verificamos el estado inicial del restaurante
        print(f"Restaurante: {restaurante_prueba.nombre}, Calificación Inicial: {restaurante_prueba.calificacion}")

        # Simulamos la recepción de pedidos
        restaurante_prueba.recibir_pedidos(clientes_prueba)

        # Verificamos la calificación después de atender a los clientes
        print(f"Calificación Final del Restaurante: {restaurante_prueba.calificacion:.2f}")

    except ValueError as e:
        print(e)
    except TypeError:
        print("Hay una cantidad incorrecta de argumentos en algún inicializador y/o todavía no defines una clase")
    except AttributeError:
        print("Algún atributo está mal definido y/o todavía no defines una clase")
