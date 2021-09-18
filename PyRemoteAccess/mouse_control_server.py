from threading import Thread
import pyautogui
import socket, keyboard
import time

ip_port = ("192.168.1.2", 52000)
class keyboard_control:
    def __init__(self, ip_port):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind(ip_port)
        s.listen(5)
        self.conn, addr = s.accept()

        while True:
            Thread(target = self.mouse).start()
            Thread(target = self.keyboard).start()
    def mouse(self):
        w = pyautogui.position()
        x_mouse = w.x
        y_mouse = w.y
        print(x_mouse, y_mouse)
        self.conn.send(str(x_mouse).encode())
        self.conn.send(str(y_mouse).encode())
        time.sleep(0.1)
    def keyboard(self):
        with Listener(on_release= self.show) as listener:
                listener.join()
    def show(self, key):
        key1 = str(key)
        print(key)

        self.conn.send(key1.encode())
app = keyboard_control(ip_port)
