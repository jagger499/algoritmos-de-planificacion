class Proceso:
    def __init__(self, nombre, tiempo_restante):
        self.nombre = nombre
        self.tiempo_restante = tiempo_restante

    def ejecutar(self, tiempo):
        print("Ejecutando proceso", self.nombre, "durante", tiempo, "unidades de tiempo")

class RoundRobin:
    def __init__(self, quantum):
        self.quantum = quantum
        self.cola = []

    def agregar_proceso(self, proceso):
        self.cola.append(proceso)

    def ejecutar(self):
        tiempo_total = 0

        while len(self.cola) > 0:
            proceso_actual = self.cola.pop(0)
            tiempo_ejecucion = min(self.quantum, proceso_actual.tiempo_restante)
            tiempo_total += tiempo_ejecucion

            proceso_actual.ejecutar(tiempo_ejecucion)
            proceso_actual.tiempo_restante -= tiempo_ejecucion

            if proceso_actual.tiempo_restante > 0:
                self.cola.append(proceso_actual)

            # Esperar el tiempo necesario para ejecutar la siguiente tarea
            tiempo_total += 1

        print("Tiempo total de ejecución:", tiempo_total)



rr = RoundRobin(3)  # Quantum de 3 unidades de tiempo

# Crear procesos
p1 = Proceso("Proceso 1", 6)
p2 = Proceso("Proceso 2", 4)
p3 = Proceso("Proceso 3", 8)

# Agregar procesos a la cola
rr.agregar_proceso(p1)
rr.agregar_proceso(p2)
rr.agregar_proceso(p3)

# Ejecutar planificación Round Robin
rr.ejecutar()
