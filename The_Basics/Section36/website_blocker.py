import time
from datetime import datetime as dt

# admin_hosts_path = r"C:\Windows\System32\drivers\etc\hosts"
temp_hosts_path = "C:\Users\ilale\Personal\Python\ThePythonMegaCourse\The_Basics\Section36\hosts"
    
redirect = "127.0.0.1"

website_list = ["www.facebook.com", "facebook.com"]

while True:
    year = dt.now().year
    month = dt.now().month
    day = dt.now().day
    if dt(year, month, day, 10) < dt.now() < dt(year, month, day, 19):
        print("Working hours...")
    else: print("Non-working hours...")
    
    # print("Working hours...") if dt(year, month, day, 10) < dt.now() < dt(year, month, day, 19) else print("Non-working hours...")
    time.sleep(2)