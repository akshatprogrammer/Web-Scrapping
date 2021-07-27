# importing Libraries -> Akshat Jain
import requests
import json
from datetime import datetime, timedelta
# Logic for time and  converting it into proper DD/MM/YY format -> Anjali Pathak
today = datetime.today()

pin = input("Enter Pin: ")  # inputting PINCODE

# Logic to get time 
num_day = 7
all_dates = []

for i in range(num_day):
    all_dates.append(today+timedelta(i))

final_dates=[]

for i in all_dates:
    final_dates.append(i.strftime("%d%m%y"))
    
# Web Scrapping Logic -> Akshat Jain
while(True):
    for d in final_dates:
        URL = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode={}&date={}".format(pin,d)
        result = requests.get(URL)
        json_result = result.json()

        if json_result["centers"]:
                for center in json_result["centers"]:
                    for session in center["sessions"]:
                        print("pincode: "+pin)
                        print("date: "+d)
                        print("Center Name: ", center["name"])
                        print("Center Address: ",center["address"])
                        print("\n")
