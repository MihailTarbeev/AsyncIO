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
connection, client_address = server_socket.accept()
print(f'Получен запрос на подключение от {client_address}')
