"""
从客户端传递一张图片给服务端，在服务端
以当前日期为名字保存起来
"""
from socket import *
import time
tcp_sk=socket(AF_INET,SOCK_STREAM)
tcp_sk.bind(("0.0.0.0",3180))
tcp_sk.listen(5)
print("waiting for you")
while True:
    connfd,addr=tcp_sk.accept()
    print("link:",addr)
    while True:
        name=str(time.strftime('%Y-%m-%d'))
        pic=open(name+".jpg","ab")
        data=connfd.recv(1024)
        if data==b"##":
            break
        pic.write(data)
    pic.close()
    connfd.send("上传完成".encode())
    connfd.close()

tcp_sk.close()