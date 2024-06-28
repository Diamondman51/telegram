import json


def filtering(user, message, to, user_socket=None):
    data = {
        'user': user,
        'message': message,
        'user_socket': user_socket,
        'to': to
    }

    return json.dumps(data).encode()

# pr = filtering('java', 'fs', 'fea')
# print(type(pr))
# pr = json.loads(pr)
# print(pr['user'])

# name = 'java'
# name = name.encode()
# print(name)
# # print(json.dumps({'header': b'7         ', 'data': b'Java'}).encode())
#
# print(type(filtering(name.decode(), 'bla', 'killer')))