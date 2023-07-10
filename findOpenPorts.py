import socket
import time

# function for logging
def logText(message, filename):
    lg = open(filename, 'a') # open a txt file to write in
    current_time = time.strftime('%H:%M:%S', time.localtime()) #set current time
    lg.write(f'{current_time} - {message} \n') # write message into textfile
    lg.close() # close file

def checkPOI(HOST, logFileAll, logFileOpen):
    PORTS = [21, 25, 80, 502] # TCP ports

    logText(f'Connetion to: {HOST}', logFileAll)
    logText(f'Connetion to: {HOST}', logFileOpen)
    print(f'Connection to: {HOST}')
    for arg in PORTS:
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.connect((HOST, arg))
                logText(f'Port: {arg} OPEN', logFileAll)
                logText(f'Port: {arg}', logFileOpen)
                print(f"Port: {arg} OPEN")
                s.close()
        except:
            logText(f'Port: {arg} CLOSED', logFileAll)
            print(f'Port: {arg} CLOSED')


def bruteForcePortSearch(HOST, logFileAll, logFileOpen): # Function to brute Force oben PORTS
    logText(f'Connection to: {HOST}', logFileAll)
    logText(f'Connection to: {HOST}', logFileOpen)
    print(f"Connection to: {HOST}")
    PORT = 0 # Define start Index of searched Ports (privileged ports normaly are <= 1023)
    while True:
        if PORT > 1023: break # Define end Index of searched Ports
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.connect((HOST, PORT))
                logText(f'Port: {PORT} OPEN', logFileAll)
                logText(f'Port: {PORT} OPEN', logFileOpen)
                print(f"Port: {PORT} OPEN")
                s.close()
        except:
            logText(f'Port: {PORT} CLOSED', logFileAll)
            print(f'Port: {PORT} CLOSED')
        PORT=PORT+1


if __name__ == '__main__':
    logAll = 'loggerPorts.txt' # name of log with all Ports
    logOpen = 'loggerOpenPorts.txt' # name of log with Open Ports
    HOST = '127.0.0.1'
    # HOST = '169.254.173.4' # Insert IP form HOST of interest
    checkPOI(HOST, logAll, logOpen)
    bruteForcePortSearch(HOST, logAll, logOpen)