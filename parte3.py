import time
import random


class Nodo:

    def __init__(self, nombre):
        self.nombre = nombre
        self.conexiones = []
        self.buffer = []

    def agregar_conexion(self, nodo):
        self.conexiones.append(nodo)
        print(f"Conexión establecida: {self.nombre} <-> {nodo.nombre}")

    def eliminar_conexion(self, nodo):
        if nodo in self.conexiones:
            self.conexiones.remove(nodo)
            print(f"Conexión eliminada: {self.nombre} -X- {nodo.nombre}")

    def enviar_mensaje(self, mensaje):
        print(f"\n[{self.nombre}] Enviando mensaje: '{mensaje}'")

        if not self.conexiones:
            print(f"[{self.nombre}] No hay nodos conectados.")
            return

        for nodo_destino in self.conexiones:
            nodo_destino.recibir_mensaje(self.nombre, mensaje)

    def recibir_mensaje(self, remitente, mensaje):

        if random.random() < 0.3:
            print(f"[{self.nombre}] ❌ Paquete perdido de '{remitente}'")
            return

        print(
            f"[{self.nombre}] Mensaje recibido de '{remitente}': '{mensaje}' (en buffer)"
        )
        self.buffer.append((remitente, mensaje))

    def procesar_buffer(self):

        print(f"\n[{self.nombre}] Procesando buffer...")

        while self.buffer:
            remitente, mensaje = self.buffer.pop(0)
            print(f"[{self.nombre}] Procesado mensaje de '{remitente}': '{mensaje}'")


def main():
    servidor = Nodo("Servidor")
    cliente1 = Nodo("Cliente1")
    cliente2 = Nodo("Cliente2")
    cliente3 = Nodo("Cliente3")

    servidor.agregar_conexion(cliente1)
    servidor.agregar_conexion(cliente2)
    servidor.agregar_conexion(cliente3)

    servidor.enviar_mensaje("Hola a todos los clientes conectados!")
    servidor.enviar_mensaje("La conexión funciona correctamente.")

    print("\nSimulando desconexión y reconexión dinámica...")

    servidor.eliminar_conexion(cliente2)

    time.sleep(2)

    servidor.agregar_conexion(cliente2)

    servidor.enviar_mensaje("¡Hola de nuevo a todos!")

    cliente1.procesar_buffer()
    cliente2.procesar_buffer()
    cliente3.procesar_buffer()


if __name__ == "__main__":
    main()
