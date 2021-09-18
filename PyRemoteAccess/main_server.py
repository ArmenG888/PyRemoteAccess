from screen_server import screen_server
from mouse_control_server import mouse_server
from keyboard_control_server import keyboard_server
if __name__ == "__main__":
    screen_server = screen_server.__init__("127.0.0.1",52000)
    mouse_server = mouse_server.__init__("127.0.0.1",52001)
    keyboard_server = keyboard_server.__init__("127.0.0.1",52002)
