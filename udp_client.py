
import socket

# Configurar el cliente
UDP_IP = "127.0.0.1"  # Dirección IP del servidor
UDP_PORT = 5005       # Puerto del servidor

# Crear el socket UDP
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Enviar un mensaje al servidor
message = "¡Hola, servidor UDP!"
client_socket.sendto(message.encode(), (UDP_IP, UDP_PORT))

# Recibir respuesta del servidor
response, server_addr = client_socket.recvfrom(1024)
print(f"Respuesta del servidor: {response.decode()}")

# Cerrar el socket
client_socket.close()
