from threading import Thread
import socket
from pynput.mouse import Listener
import time

ip_port = ("192.168.1.2", 52000)
class keyboard_control:
    def __init__(self, ip_port):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind(ip_port)
        s.listen(5)
        self.conn, addr = s.accept()
        with Listener(on_move=self.on_move, on_click=self.on_click, on_scroll=self.on_scroll) as listener:
            listener.join()
    def on_move(self,x, y):
        self.conn.send("move,".encode() + str(x+","+y).encode())


    def on_click(self,x, y, button, pressed):
        self.conn.send("click".encode())

    def on_scroll(self,x, y, dx, dy):
        print(x, y, dx, dy)
app = keyboard_control(ip_port)
