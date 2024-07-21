import json


def filtering(name, message, from_, to):
    data = {
        'name': name,
        'message': message,
        'from': from_,
        'to': to
    }

    return json.dumps(data).encode()
