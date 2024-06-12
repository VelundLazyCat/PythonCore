import base64


def encode_data_to_base64(data):
    base64_list = []
    for password in data:
        message_bytes = password.encode("utf-8")
        base64_bytes = base64.b64encode(message_bytes)
        base64_list.append(base64_bytes.decode("utf-8"))
    return base64_list
