import socket
import models.rocket as rocketlib

class Launcher:
    def __init__(self,host,port):
        self.host = host
        self.port = port
    
    def launch(self):
        # Launcher Setting
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as connection:
            try:
                message = "Set Launcher"
                try:
                    print(f"\033[1;33m[Pending] \033[0;0m{message}",end="\r")
                    connection.connect((self.host, self.port))
                    print(f"\033[0;32m[Done] \033[0;0m{message}   ",end="\n")
                except:
                    print(f"\033[0;31m[Failed] \033[0;0m{message}    ",end="\n")

                rocket = rocketlib.Rocket()
                while True:
                    rocket.launch(connection)        
            except:
                message = "Launcher Shutting Down, Bye!"
                try:
                    print(f"\033[1;33m[Pending] \033[0;0m{message}",end="\r")
                    connection.close()
                    print(f"\033[0;32m[Done] \033[0;0m{message}   ",end="\n")
                except:
                    print(f"\033[0;31m[Failed] \033[0;0m{message}    ",end="\n")

