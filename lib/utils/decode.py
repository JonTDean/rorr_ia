import re

def decode_form_data(data):
    readable_strings = re.findall(b'[ -~]{4,}', data)
    decoded_strings = [s.decode('utf-8') for s in readable_strings]
    binary_data = [byte for byte in data if byte not in readable_strings]
    interpreted_binary_data = [int(byte) for byte in binary_data]
    return {"readable_strings": decoded_strings, "binary_data": interpreted_binary_data}
