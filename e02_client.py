from socket import *
import time
tcp_sk=socket()
address=("127.0.0.1",3180)
tcp_sk.connect(address)
file=open("jinyuzhen.jpg","rb")
while True:
    pic=file.read(1024)
    if not pic:
        time.sleep(0.1)
        tcp_sk.send(b"##")
        break
    tcp_sk.send(pic)
file.close()
result=tcp_sk.recv(1024)
print(result.decode())
tcp_sk.close()