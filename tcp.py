import socket

target_host ="www.google.com"
target_port = 80

#socket creation
clinet = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#connect 

clinet.connect((target_host,target_port))

#send some data

data ="GET / HTTP/1.1\r\nHost: google.com\r\n\r\n"
clinet.send(data.encode('utf-8'))


 #receive some data
 
response = clinet.recv(4096).decode('utf-8')

print (response)
