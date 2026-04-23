class Nodo:

    def __init__(self, nombre):
        self.nombre = nombre
        self.conexiones = []

    def agregar_conexion(self, nodo):
        self.conexiones.append(nodo)
        print(f"Conexión establecida: {self.nombre} <-> {nodo.nombre}")

    def enviar_mensaje(self, mensaje):
        print(f"\n[{self.nombre}] Enviando mensaje: '{mensaje}'")

        if not self.conexiones:
            print(f"[{self.nombre}] No hay nodos conectados.")
            return

        for nodo_destino in self.conexiones:
            nodo_destino.recibir_mensaje(self.nombre, mensaje)

    def recibir_mensaje(self, remitente, mensaje):
        print(f"[{self.nombre}] Mensaje recibido de '{remitente}': '{mensaje}'")


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


if __name__ == "__main__":
    main()
