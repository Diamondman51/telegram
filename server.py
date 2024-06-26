

import socket

import select

PORT = 1234
IP = 'localhost'
HEADER_LENGTH = 10

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server_socket.bind((IP, PORT))

server_socket.listen()

sockets_list = [server_socket]

clients = {}


def receive_message(client_socket):
    try:
        message_header = client_socket.recv(HEADER_LENGTH)


        if not len(message_header):
            return False

        message_length = int(message_header.decode('utf-8').strip())

        return {'header': message_header, 'data': client_socket.recv(message_length)}
    except:
        return False


while True:
    read_socket, _, exception_socket = select.select(sockets_list, [], sockets_list)

    for notified_socket in read_socket:
        if notified_socket == server_socket:
            client_socket, client_address = server_socket.accept()

            # Birinchi bo'lib ismni jonatish kera jonatadigan socketdan
            user = receive_message(client_socket)

            if user is False:
                continue

            sockets_list.append(client_socket)
            clients[client_socket] = user
            print(clients)

        else:
            message = receive_message(notified_socket)

            if message is False:
                sockets_list.remove(notified_socket)
                del clients[notified_socket]
                continue

            user = clients[notified_socket]

            for client_socket in clients:
                if client_socket != notified_socket:
                    client_socket.send(user['header'] + user['data'] + message['header'] + message['data'])


    for notified_socket in exception_socket:
        sockets_list.remove(notified_socket)
        del clients[notified_socket]




