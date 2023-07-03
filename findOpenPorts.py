import socket

def bruteForcePortSearch(HOST): # Function to brute Force oben PORTS
    print(f"Connection to: {HOST}")
    PORT = 0 # Define start Index of searched Ports (privileged ports normaly are <= 1023)
    while True:
        if PORT > 1023: break # Define end Index of searched Ports
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.connect((HOST, PORT))
                print(f"Port: {PORT} OPEN")
                s.close()
        except:
            print(f'Port: {PORT} CLOSED')
        PORT=PORT+1


if __name__ == '__main__':
    HOST = '127.0.0.1' # Insert IP form HOST of interest
    bruteForcePortSearch(HOST)