import socket
import keyboard

class keyboard_client:
    def __init__(self, ip="127.0.0.1",port=52002):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.connect((ip,port))
        while True:
            key = s.recv(1024).decode()
            if "'" in key:
                key = key.replace("'", "",2)
            elif "Key." in key:
                key = key.replace("Key.", "")
            keyboard.press_and_release(key)
