import socket
import keyboard
import pyautogui
import time
class mouse_client:
    def __init__(self,ip_port=("127.0.0.1",52001)):
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
