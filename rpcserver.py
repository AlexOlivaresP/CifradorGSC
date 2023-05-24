import logging
import xmlrpc.server

logging.basicConfig(filename='/bitacora.log', level=logging.DEBUG,filemode='w', 
                    format='%(asctime)s | %(levelname)s:%(message)s | %(threadName)s | %(funcName)s | %(lineno)d|')

def cifrado(texto,desplazamiento):
    texto = texto.upper()
    alfabeto = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
    cifrado = ""
    for letra in texto:
        if letra in alfabeto:
            posicion = alfabeto.find(letra)
            nueva_posicion = (posicion + desplazamiento) % 27
            cifrado += alfabeto[nueva_posicion]
        else:
            cifrado += letra
    return cifrado

def handle_connection(client_ip):
    # Registra la conexión en la bitácora
    logging.info(f"Cliente {client_ip} se ha conectado")

try:
    logging.debug("Iniciando servidor")
    server = xmlrpc.server.SimpleXMLRPCServer(("192.168.1.75", 3312))
    logging.debug("Servidor iniciado")
except:
    logging.debug("No se pudo iniciar el servidor")
    print("No se pudo iniciar el servidor")

print("Esperando consultas de cifrado... en la IP: 192.168.1.75 y puerto: 3312")

server.register_function(handle_connection, "_dispatch")

server.register_function(cifrado, "cifrado")

server.serve_forever()


