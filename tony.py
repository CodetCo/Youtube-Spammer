import socks
import socket
import time
from stem.control import Controller
from stem import Signal
import requests
from bs4 import BeautifulSoup
from subprocess import Popen, PIPE
import stem.connection
import stem.socket


# This should all work, assuming you have your tor config file set up correctly: For more information, see:https://stem.torproject.org/index.html
err = 0
counter = 0
control_socket = stem.socket.ControlPort(port = 9051)
## Basic Python Request Spammer With Tor
with Controller.from_port(port = 9151) as controller:
    try:
        controller.authenticate()
        socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, "127.0.0.1", 9150)
        socket.socket = socks.socksocket
        while counter < 100:
            r = requests.get("https://www.youtube.com/watch?v=K9eRHaydIjI&list=PLEFX-UjITBKdfICF-K6HvtMVrZTa-F0Qh&index=2&t=0s")
            counter = counter + 1
            ##Is tor ready?
            controller.signal(Signal.NEWNYM)
            time.sleep(controller.get_newnym_wait())
            time.sleep(20);
    except requests.HTTPError:
        print("Could not reach URL")
        err = err + 1
print("Used " + str(counter) + " IPs and got " + str(err) + " errors")

