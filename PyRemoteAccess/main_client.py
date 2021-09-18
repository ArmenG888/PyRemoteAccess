#from screen_client import screen_client
from mouse_control_client import mouse_client
from keyboard_control_client import keyboard_client
ip = "192.168.1.2"
if __name__ == "__main__":
    #screen_client = screen_client.__init__(ip,52000)
    mouse_client = mouse_client.__init__((ip,52001))
    keyboard_client = keyboard_client.__init__(ip,52002)
