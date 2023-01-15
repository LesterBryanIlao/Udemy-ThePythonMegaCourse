import time
from datetime import datetime as dt

# admin_hosts_path = r"C:\Windows\System32\drivers\etc\hosts"
temp_hosts_path = r"C:\Users\ilale\Personal\Python\ThePythonMegaCourse\The_Basics\Section36\hosts"
    
redirect = "127.0.0.1"

website_list = ["www.facebook.com", "facebook.com", "www.twitter.com", "twitter.com"]

while True:
    year = dt.now().year
    month = dt.now().month
    day = dt.now().day
    
    if dt(year, month, day, 10) < dt.now() < dt(year, month, day, 19):
        file = open(temp_hosts_path, "r+")
        content = file.read()
        
        for website in website_list:
            if website in content:
                pass
            else:
                file.write(redirect+" "+website+"\n")
                
        print("Working hours...")
        
    else: 
        file = open(temp_hosts_path, "r+")
        content = file.readlines()
        
        file.seek(0)
        
        for line in content:
            if not any(website in line for website in website_list):
                file.write(line)
                
        file.truncate()
        print("Fun hours...")
    time.sleep(2)