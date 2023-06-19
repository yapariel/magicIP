import requests
import time

def iphunt():
    while True:
        try:
            response = requests.get("http://google.com", proxies={"http": "http://google.com:80"}, timeout=5)
            if "msisdn" in response.text:
                print("YOU'RE GOOD TO GO!")
                break
            else:
                print("TRY TURN OFF/ON AIRPLANE MODE", end="\r")
        except requests.exceptions.RequestException:
            print("TRY TURN OFF/ON AIRPLANE MODE", end="\r")
        
        time.sleep(1)

iphunt()
