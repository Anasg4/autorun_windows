
import winreg as reg
import sys
from winreg import *


def AddToRegistry():

    key_value = "Software\Microsoft\Windows\CurrentVersion\Run"

    open = reg.OpenKey(reg.HKEY_CURRENT_USER, key_value, 0, reg.KEY_ALL_ACCESS)

    reg.SetValueEx(open, queryvalue , 0, reg.REG_SZ, address)

    # close the opened key
    reg.CloseKey(open)


def checkreg():

    key_value = "Software\Microsoft\Windows\CurrentVersion\Run"

    try:
        open = reg.OpenKey(reg.HKEY_CURRENT_USER, key_value, 0, reg.KEY_ALL_ACCESS)
        OpenKey(reg.HKEY_CURRENT_USER, key_value)
        reg.QueryValueEx(open, queryvalue)
        ask = input("Your query value available on your windows registry, wanna add another query ? (y/n) ")
        if ask == "y":
            value()
        elif ask == "n":
            print("Sayonara <3")
            sys.exit()
        else:
            print("bruh... bye")
            sys.exit()

    except:
       pass

def value():
    address = input("""
Type Your application/software location 
Example >> D:\program\software.exe
>> """)
    queryvalue = input("type your random query value  : ")
    return address,queryvalue


if __name__ == "__main__":
    address, queryvalue = value()
    # check the queryvalue exist in windows registry
    checkreg()
    # add the queryvalue in windows registry
    AddToRegistry()
    print("Now Your App/software will auto running when windows turned on")
    sys.exit()
