from threading import Thread
import socket
from pynput.mouse import Listener
import time

class mouse_server:
    def __init__(self, ip="127.0.0.1",port=52001):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((ip,port))
        s.listen(5)
        self.conn, addr = s.accept()
        with Listener(on_move=self.on_move, on_click=self.on_click, on_scroll=self.on_scroll) as listener:
            listener.join()
    def on_move(self,x, y):
        message = "move," + str(x)+","+str(y)
        self.conn.send(message.encode())
        time.sleep(0.05)
    def on_click(self,x, y, button, pressed):
        self.conn.send("click".encode())

    def on_scroll(self,x, y, dx, dy):
        print(x, y, dx, dy)

mouse_server = mouse_server()
