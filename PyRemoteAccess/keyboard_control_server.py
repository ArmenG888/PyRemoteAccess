from pynput.keyboard import Key, Listener
import socket, keyboard

ip_port = ("192.168.1.2", 52001)
class keyboard_control:
    def __init__(self, ip_port):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind(ip_port)
        s.listen(5)
        self.conn, addr = s.accept()
        with Listener(on_release= self.show) as listener:
                listener.join()
    def show(self, key):
        key1 = str(key)
        print(key)

        self.conn.send(key1.encode())
app = keyboard_control(ip_port)
