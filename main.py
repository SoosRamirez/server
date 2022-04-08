import socket
import logging
from logging.handlers import SysLogHandler

log = logging.getLogger('MyLogger')


def init_logger():
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    handler = SysLogHandler(address='/dev/log')
    handler.setFormatter(formatter)
    log.addHandler(handler)
    log.setLevel(logging.DEBUG)


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('localhost', 48395))
init_logger()
client = []
print('Start Server')
while True:
    data, addres = sock.recvfrom(1024)
    log.debug(data)
    print(addres[0], addres[1])
    if addres not in client:
        client.append(addres)
    for clients in client:
        if clients == addres:
            continue
        sock.sendto(data, clients)
