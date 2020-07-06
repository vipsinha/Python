import socket
import sys

# Create a TCP/IP socket
# AF_INET correspond to IPv4
# SOCK_STREAM correspond to Tcp
sock = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = (socket.gethostname(), 13400)
#print >> sys.stderr, 'starting up on %s port %s' % server_address
sock.bind(server_address)

# Listen for incoming connections
# queue for 5, if heavy load is there
sock.listen(5)

while True:
    # Wait for a connection
    # client_address is the ip address
    print ('sys.stderr, waiting for a connection')
    connection, client_address = sock.accept()
    print (f'Connection from {client_address} has been established')
    # Send the data 
    connection.send(bytes("Welcome to server!", "utf-8"))
    # Clean up the connection 
    connection.close()
# try:
#     # print >>sys.stderr, 'connection from', client_address

#     # Receive the data in small chunks and retransmit it
#     while True:
#         # data = connection.recv(16)
#         #print >>sys.stderr, 'received "%s"' % data
#         if data:
#             #print >>sys.stderr, 'sending data back to the client'
#             connection.sendall(data)
#         else:
#             #print >>sys.stderr, 'no more data from', client_address
#             break
        
# finally:
#     
