
import socket

socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

socket.connect(('localHost',5656))

print("Iniciamos Cliente!") 

while True: 
    mensajeCliente = input("Cliente dice: ")

    socket.send(mensajeCliente.encode(encoding="ascii"))
    respuesta = socket.recv(1024)

    print("servidor", respuesta.decode(encoding="ascii"))

socket.close()