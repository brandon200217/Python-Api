import socket

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

server.bind(('localHost',5656))
server.listen(1)

print("SERVIDOR EN ESPERA!")

conexion,direccion = server.accept()



while True:
    respuesta = conexion.recv(1024).decode(encoding="ascii")

    print("cliente dice: ",respuesta)

    enviar=input("Server dice: ")

    conexion.send(enviar.encode(encoding="ascii"))
    
    breakConexion = input("Quires romper la Conexion: SI/NO ")

    if (breakConexion ==  "SI"):
        
        break

conexion.close()