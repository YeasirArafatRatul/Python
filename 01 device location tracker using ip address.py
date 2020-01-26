import requests
import socket
from datetime import datetime
import time
 
def tracker():
    try:
        ip = socket.gethostbyname("Your Site Link")
        today = datetime.now()
        date_time = today.strftime("%m_%d_%Y_%H_%M_%S")
 
        if ip != None:
            api_endpoint = f"your site link"
               
            data = requests.get(api_endpoint).json()  
        rsp = data['rsp']
           
    finally:
        #time.sleep(1800)
        tracker()
       
       
 
tracker()
