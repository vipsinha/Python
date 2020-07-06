import socket
import sys

# Create a TCP/IP socket
# AF_INET correspond to IPv4
# SOCK_STREAM correspond to Tcp
sock = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)

sock.connect((socket.gethostname(), 13400))

full_msg = ''

while True:
    msg = sock.recv(8)
    if len(msg) <= 0:
        break
    full_msg  +=  msg.decode("utf-8")
print(full_msg)
