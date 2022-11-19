import pywhatkit 
import pyautogui as pg
import time
from datetime import datetime

x=1
y=1
try: 
    while x==1:
        y=1
        now = datetime.now()
        chour=now.strftime("%H")
        mobile=input("Enter mobile no: ")
        while y==1:
            x=1
            y=1
            message=input("Enter message: ")
            hour =int(input("Enter hour : "))
            minute = int(input("Enter minute: "))
            if( pywhatkit.sendwhatmsg(mobile,message,hour,minute)):
                print("")
            else:
                time.sleep(1)
                with pyautogui.hold('Alt'):
                    pyautogui.press(['f4'])
                print("SUCCESSFUL")
            don=input("Do you want Send Another Message: (Y/N)\n")
            if don=='Y' or don == 'y':
                print("YES DEDİK BAŞKA MESAJA")
                no=input("Do you want Send Message to Same Person : (Y/N)")
                if no == 'Y' or no == 'y':
                    x=2
                    print("AYNI KİŞİYE YES DEDİK")
                else:
                    print("AYNI KİŞİYE NO DEDİK")
                    y=2
            else:
                print("NO DEDİK BAŞKA MESAJA")
                x=2
                y=2
except:
    print("Error!!!")
    time.sleep(5)
    print("PROGRAM İS SHUTDOWNİNG")
    time.sleep(5)


    
        
