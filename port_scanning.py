import socket
import sys

def port_scanning(remote_host):
    try:
        for port in range(1, 254 + 1):
            tcp_socket = socket.socket(socket.AF_INET,
                                       socket.SOCK_STREAM)

            data = tcp_socket.connect_ex((remote_host, port))
            if data == 0:
                print("[+] Open {}:::{}".format(port, socket.getservbyport()))
            else:
                print(data)
            return
            
    except socket.gaierror:
        print("[-] Host remoto nao encontrado")
        exit()
    except socket.error:
        print("[-] Erro durante o socket")
        exit()

def main():
    if sys.argv[1] == '-h':
        print('python3 port_scanning.py [host]')
    else:
        remote_host = sys.argv[1]
        port_scanning(remote_host)

if __name__ == "__main__":
    main()