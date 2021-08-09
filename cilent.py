from socket import *

SERVER_PORT = 55555
BUFSIZE = 1024

def main():
    host = input("Server-Adresse: ")
    msg = input("Nachricht (a für Shutdown): ")
    s = socket(AF_INET, SOCK_STREAM)
    s.connect((host, SERVER_PORT))
    s.send(msg)
    s.close()
    
main()
