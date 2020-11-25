import socket
import threading
 b_ip = "localhost"
 b_port = 9999

 s = socket.socket(socket.AF_INET,socket,SOCK_STREAM)

 s.bind((b_ip,b_port))

s.listen(5)

print "[*] Listening on %s:%d" % (b_ip,b_port)

def h_clinet(c_socket):
        req =  c_socket.recv(1024)
       
print "[*] Recevied: %s" % req

c_socket.send("ACK!")
c_socket.close()

while True:
client,addr = s.accept()

print "[*]  Accepted connection from: %s: %d" % (addr[0],addr[1])

client_handler = theading.Thread(target=h_client,args=(client,))

client_handler.start()
