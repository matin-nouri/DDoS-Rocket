class Rocket:
    def __init__(self):
        pass

    def launch(self,setting):
        message = "Launching a DDR1-24 Rocket to Destination"
        try:
            print(f"\033[1;33m[Pending] \033[0;0m{message}",end="\r")
            setting.sendall(b"c92182ecd5ca5547b3e60993d57c67c4f5a8f1796a34c154e95cbe9f24e9bd95b00ca22872ae5be47cd48645db95c940acb460681a72fc8d76d6f0a5963f9fa7")
            print(f"\033[0;32m[Done] \033[0;0m{message}   ",end="\n")
        except:
            print(f"\033[0;31m[Failed] \033[0;0m{message}    ",end="\n")
