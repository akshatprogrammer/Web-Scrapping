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