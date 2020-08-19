from socket import *
tcp_sk=socket(AF_INET,SOCK_STREAM)
tcp_sk.bind(("0.0.0.0",3180))
tcp_sk.listen(5)
print("waiting for you")
while True:
    connfd,addr=tcp_sk.accept()
    print("link:",addr)
    while True:
        data=connfd.recv(1024)
        if data.decode().lower()=="quit":
            print("程序终止")
            break
        print("accepted:",data.decode())
        connfd.send(b"Im OK")
    connfd.close()
# tcp_sk.close()