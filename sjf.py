class Proceso:
    def __init__(self, nombre, tiempo_ráfaga):
        self.nombre = nombre
        self.tiempo_ráfaga = tiempo_ráfaga

    def __str__(self):
        return self.nombre


class SJF:

    def __init__(self):
        self.procesos = []

    def agregar_proceso(self, nombre, tiempo_ráfaga):
        proceso = Proceso(nombre, tiempo_ráfaga)
        self.procesos.append(proceso)

    def ejecutar(self):
        # Ordenar la lista de procesos según el tiempo de ráfaga (burst time) en orden ascendente
        self.procesos.sort(key=lambda x: x.tiempo_ráfaga)

        # Ejecutar los procesos en orden
        tiempo_total = 0
        for proceso in self.procesos:
            print(f"Ejecutando proceso {proceso.nombre} durante {proceso.tiempo_ráfaga} unidades de tiempo.")
            tiempo_total += proceso.tiempo_ráfaga

        tiempo_promedio = tiempo_total / len(self.procesos)
        print(f"\nTiempo promedio de ejecución: {tiempo_promedio}")


planificador = SJF()

# Agregar procesos
planificador.agregar_proceso("P1", 6)
planificador.agregar_proceso("P2", 8)
planificador.agregar_proceso("P3", 3)
planificador.agregar_proceso("P4", 2)

# Ejecutar el algoritmo SJF
planificador.ejecutar()
