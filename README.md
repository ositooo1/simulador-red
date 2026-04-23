# simulador-red

este programa simula una red de una comunicacion entre un servidor y varios clientes

tenemos una clase nodo que representa cada dispositivo en esta red, en el init se guardan los nombres de las redes

el método agregar_conexion permite conectar un nodo con otro, agregándolo a la lista

el metodo enviar_mensaje envia un mensaje a todos los nodos conectados

el metodo recibir_mensaje muestra el mensaje recibido y quien lo envio

en la funcion main se crea un servidor y tres clientes, se conectan entre si y se mandan mensajes
^^^^^^ parte 1

parte 2>>>>>

se agrego el metodo eliminar_conexion que nos permite quitar un nodo de la lista de conexiones utilizando .remove()

se importo la libreria time para usar sleep()

luego de los primeros mensajes enviados por el servidor simulan una desconedxion y eliminacion con uno de los clientes

despues se utilizo time.sleep(2) para representar un retraso en la red

finalmente se volvio a establecer la conexion con el cliente y se envio un mensaje de vuelta
