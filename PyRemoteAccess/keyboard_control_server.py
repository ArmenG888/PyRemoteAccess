from pynput.keyboard import Key, Listener
import socket, keyboard
class keyboard_server:
    def __init__(self, ip="127.0.0.1",port=52002):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((ip_port))
        s.listen(5)
        self.conn, addr = s.accept()
        with Listener(on_release= self.show) as listener:
                listener.join()
    def show(self, key):
        key1 = str(key)
        self.conn.send(key1.encode())
