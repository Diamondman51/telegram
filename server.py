import socket

import select

PORT = 1234
IP = 'localhost'
HEADER_LENGTH = 10

my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

my_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

my_socket.bind((IP, PORT))

my_socket.listen()

sockets_list = [my_socket]


clients = {}


def receive_message(client_socket):
    try:
        message_header = client_socket.recv(HEADER_LENGTH)
        if not len(message_header):
            return False

        message_length = int(message_header.decode.strip())

        return {'length': message_length, 'text': client_socket.recv(message_length)}
    except:
        return False


while True:
    read_socket, write_socket, exception_socket = select.select(sockets_list, [], sockets_list)

    for notified_socket in read_socket:
        if notified_socket == my_socket:
            client_socket, client_address = notified_socket.accept()

            # Birinchi bo'lib ismni jonatish kera jonatadigan socketdan
            user = receive_message(client_socket)

            sockets_list.append(client_socket)
            clients[notified_socket] = user

        else:
            message = receive_message(notified_socket)

            if message is False:
                sockets_list.remove(notified_socket)
                del clients[notified_socket]
                continue

            user = clients[notified_socket]

            for client_socket in clients:
                # if client_socket != notified_socket:
                client_socket.send(user['length'] + user['text'] + message['length'] + message['text'])

    for notified_socket in exception_socket:
        sockets_list.remove(notified_socket)
        del clients[notified_socket]
