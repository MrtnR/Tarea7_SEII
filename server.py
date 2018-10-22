import socket as s

server = s.socket(s.AF_INET, s.SOCK_STREAM)

server.bind(('127.0.0.1',60000))

server.listen(5)

(client, address) = server.accept()

while True:
    
    data = client.recv(1024)
    
    print data
    
    if data == 'terminate':
        break
        
