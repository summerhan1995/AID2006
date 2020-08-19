from socket import *
addr=("127.0.0.1",3182)
while True:
    tcp_sk = socket()
    tcp_sk.connect(addr)
    words=input(">>")
    tcp_sk.send(words.encode())
    answer=tcp_sk.recv(1024)
    print(answer.decode())
    tcp_sk.close()