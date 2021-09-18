import socket
import keyboard
import pyautogui
import time
ip_port = ("192.168.1.2", 52000)
class client:
    def __init__(self, ip_port):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.connect(ip_port)
        while True:
            packet = s.recv(1024).decode()
            packet_1 = packet.split(",")
            if packet_1[0] == "move":
                pyautogui.moveTo(packet_1[1],packet_1[2])
            else:
                pyautogui.click()
app = client(ip_port)
