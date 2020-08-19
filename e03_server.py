from socket import *
tcp_sk=socket()
tcp_sk.bind(("0.0.0.0",3182))
tcp_sk.listen(5)
dic={"你多大啦":"2岁啦","你是男生女生":"我是机器人",
     "你漂亮么":"我天生丽质"}
while True:
    print("waiting for you")
    connfd,addr=tcp_sk.accept()
    print(addr)
    data=connfd.recv(1024)
    for key in dic:
        if data.decode()==key:
            connfd.send(dic[key].encode())
            break
    else:
        connfd.send("人家还小，还不懂".encode())
    connfd.close()