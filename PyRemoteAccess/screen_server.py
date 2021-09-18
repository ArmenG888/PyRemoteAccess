import socket
import pygame
from zlib import decompress
WIDTH = 1900
HEIGHT = 1000
class screen_server:
    def __init__(self, ip="127.0.0.1", port=52002):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind((ip, port))
        print("Listening ....")
        sock.listen(5)
        conn, addr = sock.accept()
        print("Accepted ....", addr)
        pygame.init()
        screen = pygame.display.set_mode((WIDTH, HEIGHT))
        clock = pygame.time.Clock()
        watching = True
        try:
            while watching:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        watching = False
                        break
                size_len = int.from_bytes(conn.recv(1), byteorder='big')
                size = int.from_bytes(conn.recv(size_len), byteorder='big')
                pixels = decompress(self.recvall(conn, size))
                img = pygame.image.fromstring(pixels, (WIDTH, HEIGHT), 'RGB')
                screen.blit(img, (0, 0))
                pygame.display.flip()
                clock.tick(60)
        finally:
            #print("PIXELS: ", pixels)
            sock.close()
    def recvall(self,conn,length):
        buf = b''
        while len(buf) < length:
            data = conn.recv(length - len(buf))
            if not data:
                return data
            buf += data
        return buf
screen_server = screen_server()
