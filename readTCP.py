# I use this script to read a TCP data package and see how it looks
import socket
import time

__HOST = '169.254.173.4'
__PORT = 22
def logText(message, filename):
    lg = open(filename, 'a') # open a txt file to write in
    current_time = time.strftime('%H:%M:%S', time.localtime()) #set current time
    lg.write(f'{current_time} - {message} \n') # write message into textfile
    lg.close() # close file

# Read data from Logger
def readData(HOST, PORT):
    try:
        with socket.socket(socket.AF_Inet, socket.SOCK_Stream) as s:
            s.connect(HOST, PORT)
            data = s.recv(1024).decode('utf-8')
            return data
    except:
        logText(f'Host: {HOST}; Port: {PORT} could not establish connection', 'NO CONNECTION')

if __name__ == '__main__':
    logText(readData(__HOST, __PORT), 'dataTCP.txt')