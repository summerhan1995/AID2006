"""
author: Grace
email:1377070322@qq.com
time:2020-8-14
env: Python 3.6
socket and Process
"""
from socket import *
from multiprocessing import *
ADDR=("0.0.0.0", 5555)
dict={}
def login(result,udp_sk,addr):
    if result[1] in dict or "管理" in result[1]:
        udp_sk.sendto("用户已存在".encode(), addr)
    else:
        udp_sk.sendto("ok".encode(), addr)
        msg="欢迎%s进入聊天室"%result[1]
        for key in dict:
            udp_sk.sendto(msg.encode(),dict[key])
        dict[result[1]] = addr
def chat(sock,name,content):
    msg="%s : %s"%(name,content)
    for i in dict:
        if i!=name:
            sock.sendto(msg.encode(),dict[i])
def exit(sock,name):
    del dict[name]
    msg="%s 退出了聊天室"%name
    for i in dict:
        sock.sendto(msg.encode(),dict[i])
def request(udp_sk):
    while True:
        data, addr = udp_sk.recvfrom(1024)
        result=data.decode().split(" ",2)
        if result[0]=="L":
            login(result,udp_sk,addr)
        elif result[0]=="C":
            chat(udp_sk,result[1],result[2])
        elif result[0]=="E":
            exit(udp_sk,result[1])
def main():
    udp_sk = socket(AF_INET, SOCK_DGRAM)
    udp_sk.bind(ADDR)
    p=Process(target=request,args=(udp_sk,))
    p.daemon=True
    p.start()
    while  True:
        content=input("管理员消息：")
        msg="C 管理员消息 "+content
        udp_sk.sendto(msg.encode(),ADDR)



if __name__ == '__main__':
    main()
