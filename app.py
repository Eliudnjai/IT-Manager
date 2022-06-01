def main():
    import os
    import time
    import platform
    
    
    ip_list = ['8.8.8.8']
    for ip in ip_list:
        print("monitoring..........................")
        response = os.popen(f"ping {ip}").read()
        # print(response)
        fileWrite = open("response.txt", "w")
        fileWrite.write(response)
        fileWrite.close()
        
        fileRead = open("response.txt", "r")
        # print(fileRead.read())
        searchErrors = ["General failure.", "Request timed out.", "Destination host unreachable.", "ping: sendmsg: Invalid argument"]
        for x in searchErrors:
            x
        
    if(x in fileRead.read()):
        release = os.popen("ipconfig /release").read()
        print("Reconnecting........................................................................")
        time.sleep(2)
        renew = os.popen("ipconfig /renew").read()
        print("Getting IP address..................................................................")
        time.sleep(2)
        print(renew)

    else:
        print(".............................Already connected...................................")
        print(f"............................Connecting to {ip} successfully................................................")

    restart = 1
    if restart == 1:
        time.sleep(5)
        main()
    else:
        exit()

main()