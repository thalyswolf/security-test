import socket

try:
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

except Exception as e:
    print(e)
    print('Houve um erro durante a criacao do socket')
    exit()

host = ''
port = 9999

tcp_socket.bind((host, port)) # listening
tcp_socket.listen(1)

while True:
    c, addr = tcp_socket.accept()
    print('connection from {}:{}'.format(addr[0], addr[1]))
    c.close()


tcp_socket.close()