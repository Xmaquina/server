#!/usr/bin/python3.4
'''
simple socket server using threads
'''
 
import socket
import sys
import hashlib
 
class SendFile:

    def __init__(self, socket = None):
        self.socket = socket

    def save_md5(self, content):
        m = hashlib.md5()
        m.update(content.encode())
        md5_file = open("md5_file_temp.txt", 'w')
        #md5_file.write(m.digest().decode())
        print(m.digest())
        return m
        

    def send_file(self, file_name):
        with open(file_name) as f:
            content = f.read()
        print(type(content))
        print(content)
        md5 = self.save_md5(content)

    def notify_sending_md5(self):
        sent = self.socket.send(b"md5 sending")
        if sent == 0:
            raise RuntimeError("socket connection broken")

    def send_to_socket(self, content, md5):
        totalsent = 0
        while totalsent < length(content):
            sent = self.socket.send(content[totalsent:])
            if sent == 0:
                raise RuntimeError("socket connection broken")
            totalsent = totalsent + sent
        self.notify_sending_md5()
        while totalsent < length(md5):
            sent = self.socket.send(md5[totalsent:])
            if sent == 0:
                raise RuntimeError("socket connection broken")
            totalsent = totalsent + sent
        
    
def main():
    print("Call function") 
    m = SendFile()
    m.send_file("teste.txt")

if __name__ == "__main__":
    print("Starting")
    main()
