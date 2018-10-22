import socket as s

client = s.socket(s.AF_INET, s.SOCK_STREAM)

client.connect(('127.0.0.1',60000))

while True:
    to_send = input('Data to send: ')
    
    client.send(to_send)
    
    if to_send == 'terminate':
        break

