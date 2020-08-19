from socket import *
from multiprocessing import *
import sys
q1=Queue()
q2=Queue()

addr = ("127.0.0.1", 5555)
def login(udp_sk):
    while True:
        name = input("请输入您的姓名：")
        udp_sk.sendto(b"L "+name.encode(), addr)
        result, add = udp_sk.recvfrom(128)
        if result.decode()=="ok":
            print("进入聊天室")
            return name
        else:
            print("该用户已存在")
def send_msg(udp_sk,name):
    while True:
        try:
            content=input("发言:")
        except KeyboardInterrupt:
            content = "exit"
        if content=="exit":
            msg="E "+name
            udp_sk.sendto(msg.encode(),addr)
            sys.exit("退出聊天室")
        msg="C %s %s"%(name,content)
        udp_sk.sendto(msg.encode(),addr)

def main():
    udp_sk = socket(AF_INET, SOCK_DGRAM)
    name=login(udp_sk)
    p=MyProcess(udp_sk)
    p.daemon=True
    p.start()
    send_msg(udp_sk,name)


class MyProcess(Process):
    def __init__(self,udp_sk):
        self.udp_sk=udp_sk
        super().__init__()
    def recv_msg(self):
        while True:
            data,addr=self.udp_sk.recvfrom(1024*10)
            msg="\n"+data.decode()+"\n发言:"
            print(msg,end="")
    def run(self):
        self.recv_msg()


if __name__ == '__main__':
    main()




