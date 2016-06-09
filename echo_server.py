#!/usr/bin/env python

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('0.0.0.0', 8080))
s.listen(5)

print('Listening on', s.getsockname())
try:
    while True:
        client, addr = s.accept()
        data = client.recv(1024)
        if data:
            print('Sending data to client:', addr)
            client.send(data)
        client.close()
except KeyboardInterrupt:
    pass
finally:
    s.close()
