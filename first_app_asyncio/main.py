import socket

# Создать TCP-сервер с типом адреса, содержащим имя хоста и номер порта
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Возможность при перезапуске сервера использовать этот же порт
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)


# Задание адреса сокета
address = ('127.0.0.1', 8000)
server_socket.bind(address)
# Прослушивание запросов на подключение
server_socket.listen()

# Задание сокета неблокирующим
server_socket.setblocking(False)

connections = []

try:
    while True:
        try:
            connection, client_address = server_socket.accept()
            connection.setblocking(False)
            print(f'I got a connection from {client_address}!')
            connections.append(connection)
        except BlockingIOError:
            pass
        for connection in connections:
            buffer = b''

            while buffer[-2:] != b'\r\n':
                try:
                    data = connection.recv(2)
                    if not data:
                        break
                    else:
                        print(f'I got data: {data}!')
                        buffer = buffer + data
                    print(f"All the data is: {buffer}")
                except BlockingIOError:
                    pass
            connection.send(buffer)

finally:
    server_socket.close()
