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


def send_message_to_all(message, socket_list):
    for socket in socket_list:
        send_message(message, socket)


def send_message(message:dict, socket):
    message = json.dumps(message).encode()
    socket.send(message)


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
            print('user', user, type(user), client_socket)

            if user is False:
                continue

            # Converting to bytes
            data = json.dumps(user).encode()
            length = f'{len(data):<{HEADER_LENGTH}}'.encode()

            sockets_list.append(client_socket)

            # Send notification about connection of new user to all users who is online
            for client_socket in clients:
                print('Entered to share mode')
                # print('send_to client')
                # if client_socket != notified_socket:
                # client_socket.send(user['header'] + user['data'] + message['header'] + message['data'])
                # client_socket.send(user['header'] + user['data'])
                client_socket.send(length + data)

            clients[client_socket] = user['data']
            print('clients', clients)

        else:
            message = receive_message(notified_socket)
            user_info = json.dumps(message).encode()
            print('user_info 1: ', user_info)
            user_info = json.loads(user_info)
            user_info['data'] = json.loads(user_info['data'])

            if message is False:
                print('Exit')
                sockets_list.remove(notified_socket)
                del clients[notified_socket]
                continue

            user = clients[notified_socket]
            # message['data']

            for cl_socket in clients:
                print('send_to client')
                print('row', 86, clients[cl_socket], user_info['data']['to'])
                user_info = json.dumps(user_info).encode()
                # if clients[cl_socket] == user_info['data']['to']:
                # if client_socket != notified_socket:
                # client_socket.send(user['header'] + user['data'] + message['header'] + message['data'])
                cl_socket.send(user_info['header'] + user_info['data'])
                print(f'{cl_socket}, {message["header"]} + {message["data"]}')
                print('clients 2: ', clients)

    for notified_socket in exception_socket:
        sockets_list.remove(notified_socket)
        del clients[notified_socket]
