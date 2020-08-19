from socket import *
tcp_sk=socket()
address=("127.0.0.1",5656)
tcp_sk.connect(address)
while True:
    msg=input(">>")
    tcp_sk.send(msg.encode())
    if msg.lower()=="quit":
        print("程序终止")
        break
    data=tcp_sk.recv(1024)
    print("from you:",data.decode())
tcp_sk.close()