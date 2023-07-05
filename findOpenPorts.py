import socket
import time

# function for logging
def logText(message):
    lg = open('loggerPorts.txt', 'a')
    current_time = time.strftime('%H:%M:%S', time.localtime())
    lg.write(f'{current_time} - {message} \n')
    lg.close()

def checkPortsOfInterest(HOST):
    PORTS = [21, 25, 80, 502]

    logText(f'Connetion to: {HOST}')
    print(f'Connection to: {HOST}')
    for arg in PORTS:
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.connect((HOST, arg))
                logText(f'Port: {arg} OPEN')
                print(f"Port: {arg} OPEN")
                s.close()
        except:
            logText(f'Port: {arg} CLOSED')
            print(f'Port: {arg} CLOSED')


def bruteForcePortSearch(HOST): # Function to brute Force oben PORTS
    logText(f'Connection to: {HOST}')
    print(f"Connection to: {HOST}")
    PORT = 0 # Define start Index of searched Ports (privileged ports normaly are <= 1023)
    while True:
        if PORT > 1023: break # Define end Index of searched Ports
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.connect((HOST, PORT))
                logText(f'Port: {PORT} OPEN')
                print(f"Port: {PORT} OPEN")
                s.close()
        except:
            logText(f'Port: {PORT} CLOSED')
            print(f'Port: {PORT} CLOSED')
        PORT=PORT+1


if __name__ == '__main__':
    HOST = '127.0.0.1'
    # HOST = '169.254.173.4' # Insert IP form HOST of interest
    checkPortsOfInterest(HOST)
    bruteForcePortSearch(HOST)