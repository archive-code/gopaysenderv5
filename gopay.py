
import requests
from bs4 import BeautifulSoup
import os

def clear():
  if os.name == 'nt':
    os.system('cls')
  else:
    os.system('clear')

clear()
ascii = """

  _____                                            _                      
 / ____|                                          | |                     
| |  __  ___  _ __   __ _ _   _ ___  ___ _ __   __| | ___ _ __ __ _ _ __  
| | |_ |/ _ \| '_ \ / _` | | | / __|/ _ \ '_ \ / _` |/ _ \ '__/ _` | '_ \ 
| |__| | (_) | |_) | (_| | |_| \__ \  __/ | | | (_| |  __/ | | (_| | | | |
 \_____|\___/| .__/ \__,_|\__, |___/\___|_| |_|\__,_|\___|_|  \__,_|_| |_|
             | |           __/ |                                          
             |_|          |___/                                bynorahmad           

=======================================
Coded By Nor Ahmad
Github : https://github.com/archive-code
Website : http://hepiweb.fun
Instagram : http://instagram.com/norahm4d 
Note : Tools Gopay Sender Rp 8
=======================================

"""
print (ascii)
data = input("Masukkkan no hp(62xx/1xxx): ")
r = requests.post("http://gopaysender.com/server2/", data={'phone':data})
soup = BeautifulSoup(r.text, 'html.parser')

res = soup.find('div', attrs={'class':'alert'})
result = res.text.lstrip().rstrip()

def clear():
  if os.name == 'nt':
    os.system('cls')
  else:
    os.system('clear')

clear()
print(res.text)
