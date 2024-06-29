import json


def filtering(user, message, to=None, user_socket=None, data_type=1):
    data = {
        'type': data_type,  # 0 - data about entered/exited, 1 - message
        'from': user,
        'message': message,
        'to': to
    }

    return json.dumps(data).encode()

# name = 'java'.encode()
#
# pr = filtering(name, 'fs', 'fea')
# # print(type(pr))
# pr = json.loads(pr)
# print(pr)

# name = 'java'
# name = name.encode()
# print(name)
# # print(json.dumps({'header': b'7         ', 'data': b'Java'}).encode()
# print(type(filtering(name.decode(), 'bla', 'killer')))
