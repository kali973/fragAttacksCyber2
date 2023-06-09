import logging
import os
import platform
import sys
import threading


def a():
    os.system("wireshark")


def b():
    os.system('xterm -geometry 80x24+0+0 -e "sudo python balayage.py"')


def c():
    os.system('xterm -geometry 80x24-0+0 -e "sudo python configuration.py"')

def o():
    os.system('xterm -geometry 120x40 -e "sudo python retrieveMac.py"')

def x():
    os.system('xterm -e "sudo python close.py"')

def b():
    os.system('xterm -geometry 100x30+0+0 -e "sudo python balayage.py"')

def clear():
    linux = 'clear'
    windows = 'cls'
    os.system([linux, windows][os.name == 'nt'])


logging.disable(sys.maxsize)
number = 1
data = ""
command = "sudo apt-get install -y xterm > /dev/null 2>&1"
os.system(command)
os.environ['TERM'] = 'xterm'
path = os.getcwd()

while number != '0':

    data += ' ----------------------------\n'
    if os.name == "nt":
        print(' [!] Please run the script on Linux Machine !')
        quit()
    elif os.name != "nt":
        data = (' ----------------------------\n')
        data += ' Hi ' + platform.uname()[1] + '\n'

    data += ' ----------------------------\n'
    data += ' Select option:\n'
    data += ' [1] Configuration environment\n'
    data += ' [2] Scan network (Crtl-C to stop scan)\n'
    data += ' [3] Retrieve MAC address by BSSID\n'
    data += ' [4] Frag Attacks WPA2\n'
    data += ' [0] Exit\n'
    print(data)
    number = input(" Number~# ")
    if number == '1':
        print("\n Configuration environment...\n")
        threading.Thread(target=c).start()
        print("\033[H\033[J", end="")
        clear()
        data = ""
    elif number == '2':
        print("\n Scan network ...\n")
        threading.Thread(target=b).start()
        clear()
        data = ""
    elif number == '3':
        print("\n Retrieve MAC address by BSSID ...\n")
        threading.Thread(target=o).start()
        clear()
        data = ""
    elif number == '4':
        print("\n Frag Attacks WPA2 ...\n")
        # threading.Thread(target=o).start()
        clear()
        data = ""
    elif number == '0':
        print('\n [+] Good Bye ' + platform.uname()[1] + ' !\n')
        threading.Thread(target=x).start()
        clear()
        quit()
    else:
        print("\n [X] Error !\n [!] Select this number: 1, 2 or 0\n")
