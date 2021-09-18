#from screen_server import screen_server
from mouse_control_server import mouse_server
from keyboard_control_server import keyboard_server
ip = "192.168.1.2"
if __name__ == "__main__":
    #screen_server = screen_server.__init__(ip,52000)
    mouse_server = mouse_server.__init__(ip,52001)
    keyboard_server = keyboard_server.__init__(ip,52002)
