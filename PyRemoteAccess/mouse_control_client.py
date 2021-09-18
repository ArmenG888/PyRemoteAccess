import socket
import keyboard

ip_port = ("192.168.1.2", 52000)
class client:
    def __init__(self, ip_port):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.connect(ip_port)
        while True:
            key = s.recv(1024).decode()
            pyautogui.moveTo(key[0],key[1])
app = client(ip_port)
