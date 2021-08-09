from socket import *

ECHO_PORT = 55555
BUFSIZE = 1024

def main():
    s = socket(AF_INET, SOCK_STREAM)
    s.bind(('', ECHO_PORT))
    s.listen(1)
    print("Server gestartet")
    conn, (remotehost, remoteport) = s.accept()
    print('Verbunden mit %s:%s' % (remotehost, remoteport))
    data = conn.recv(BUFSIZE)
    print(data)
    s.close()
    
main()
