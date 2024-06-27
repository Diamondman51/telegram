

import socket
import select

# Doimiylar
HEADER_LENGTH = 10
IP = "127.0.0.1"
PORT = 1234

# TCP/IP soketi yaratish
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Soketni qayta ishlatish uchun sozlashlar
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Soketni manzil va portga ulash
server_socket.bind((IP, PORT))

# Kiruvchi ulanishlarni kutish
server_socket.listen()

# Kuzatiladigan soketlar ro'yxati
sockets_list = [server_socket]

# Mijozlarni va ularning ma'lumotlarini kuzatish uchun lug'at
clients = {}

def receive_message(client_socket):
    """Mijozdan xabar olish funksiyasi."""
    try:
        # Xabar sarlavhasini o'qish
        message_header = client_socket.recv(HEADER_LENGTH)

        # Agar hech qanday ma'lumot olinmasa, mijoz uzilgan
        if not len(message_header):
            return False

        # Xabar uzunligini aniqlash
        message_length = int(message_header.decode('utf-8').strip())

        # Sarlavha va ma'lumotni o'z ichiga olgan lug'atni qaytarish
        return {"header": message_header, "data": client_socket.recv(message_length)}
    except:
        return False

while True:
    # Soketlarda faoliyatni kutish uchun select funksiyasidan foydalanish
    read_sockets, _, exception_sockets = select.select(sockets_list, [], sockets_list)

    for notified_socket in read_sockets:
        if notified_socket == server_socket:
            # Yangi ulanish
            client_socket, client_address = server_socket.accept()
            user = receive_message(client_socket)

            # Agar user False bo'lsa, xabar olinmadi
            if user is False:
                continue

            # Yangi mijoz soketini kuzatiladigan soketlar ro'yxatiga qo'shish
            sockets_list.append(client_socket)

            # Foydalanuvchi ma'lumotlarini saqlash
            clients[client_socket] = user
            print(clients)

            # print(f"Yangi foydalanuvchi qo'shildi: {client_address}")
            # print(f"Olingan habar: {user['data'].decode('utf-8')}")
        else:
            # Mavjud mijozdan xabar
            message = receive_message(notified_socket)

            # Agar message False bo'lsa, mijoz uzilgan
            if message is False:
                # print(f"Aloqa uzildi: {clients[notified_socket]['data'].decode('utf-8')}")
                sockets_list.remove(notified_socket)
                del clients[notified_socket]
                continue

            # Xabarni yuborgan foydalanuvchini olish
            user = clients[notified_socket]

            # print(f"{user['data'].decode('utf-8')} foydalanuvchidan xabar olindi: {message['data'].decode('utf-8')}")

            # Xabarni barcha mijozlarga yuborish
            for client_socket in clients:
                if client_socket != notified_socket:
                    client_socket.send(user['header'] + user['data'] + message['header'] + message['data'])
                    # print('Xabar mijozga yuborildi')

    # Istisno soketlarni boshqarish
    for notified_socket in exception_sockets:
        sockets_list.remove(notified_socket)
        del clients[notified_socket]
        print("Istisno soketi o'chirildi")