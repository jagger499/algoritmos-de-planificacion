
class ColaFIFO:

    def __init__(self):
        """
        Inicializa una cola vacía.
        """
        self.cola = []

    def esta_vacia(self):
        """
        Verifica si la cola está vacía.
        el metodo len()
        True si la cola está vacía, False de lo contrario.
        """
        return len(self.cola) == 0

    def encolar(self, elemento):
        """
        Agrega un elemento al final de la cola.
        :param elemento: El elemento a agregar.
        """
        self.cola.append(elemento)

    def desencolar(self):
        if self.esta_vacia():
            raise IndexError("La cola está vacía")
        return self.cola.pop(0)

# Crear una nueva cola
cola = ColaFIFO()

# Verificar si la cola está vacía
print(cola.esta_vacia())  # True

# Agregar elementos a la cola
cola.encolar("A")
cola.encolar("B")
cola.encolar("C")

# Desencolar los elementos que anteriormente se agregaron
print(cola.desencolar())  # "A"
print(cola.desencolar())  # "B"
print(cola.desencolar())  # "C"
print(cola.esta_vacia())  # True
