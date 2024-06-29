import json
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

        return client_socket.recv(message_length).decode()
    except:
        return False


def send_message_to_all(message:dict, socket_list: list):
    for socket in socket_list:
        send_message(message, socket)


def send_message(message: dict, socket):
    message = json.dumps(message).encode()
    length = f"{len(message):<{HEADER_LENGTH}}".encode()
    print('send_message()', socket)
    socket.send(length + message)


while True:
    read_socket, _, exception_socket = select.select(sockets_list, [], sockets_list)
    print('server')

    for notified_socket in read_socket:
        print(notified_socket == server_socket)
        if notified_socket == server_socket:
            client_socket, client_address = server_socket.accept()
            print(client_socket)

            # Birinchi bo'lib ismni jonatish kera jonatadigan socketdan
            user = receive_message(client_socket)
            print('user', user, client_socket)

            if user is False:
                continue

            data = json.loads(user)

            if data['type'] == 0:

                # Converting to bytes
                data_2 = json.dumps(data).encode()
                length = f'{len(data_2):<{HEADER_LENGTH}}'.encode()

                sockets_list.append(client_socket)

                print('clients 76', clients)
                # Send notification about connection of new user to all users who is online

                for client in clients:
                    print('Entered to share mode')
                    # on for range client_socket changed to client
                    client.send(length + data_2)

                clients[client_socket] = data['from']

        else:

            data = receive_message(notified_socket)
            data = json.loads(data)
            print('data 1: ', data)

            if data is False:
                print('Exit')
                sockets_list.remove(notified_socket)
                del clients[notified_socket]
                continue

            for cl_socket in clients:
                if clients[cl_socket] == data['to']:
                    send_message(data, cl_socket)
                    print(f'{cl_socket}, {data["message"]} {data["from"]} {data["to"]}')
                    print('clients 2: ', clients[cl_socket], clients)

            # try:
            #     data = receive_message(notified_socket)
            #     data = json.loads(data)
            #     print('data 1: ', data)
            #
            #     for cl_socket in clients:
            #         if clients[cl_socket] == data['to']:
            #             send_message(data, cl_socket)
            #             print(f'{cl_socket}, {data["message"]} {data["from"]} {data["to"]}')
            #             print('clients 2: ', clients)
            # except TypeError:
            #     print('Exit')
            #     sockets_list.remove(notified_socket)
            #     del clients[notified_socket]
            #     continue

    for notified_socket in exception_socket:
        sockets_list.remove(notified_socket)
        del clients[notified_socket]
