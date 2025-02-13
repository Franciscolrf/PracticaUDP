import socket

# Configurar el servidor
UDP_IP = "127.0.0.1"  # Dirección IP local
UDP_PORT = 5005       # Puerto del servidor

# Crear el socket UDP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind((UDP_IP, UDP_PORT))

print(f"Servidor UDP escuchando en {UDP_IP}:{UDP_PORT}...")

while True:
    # Recibir datos del cliente
    data, addr = server_socket.recvfrom(1024)  # Buffer de 1024 bytes
    print(f"Mensaje recibido de {addr}: {data.decode()}")

    # Responder al cliente
    response = f"Mensaje recibido: {data.decode()}"
    server_socket.sendto(response.encode(), addr)