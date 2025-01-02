import subprocess
import wget
import os

def devices_check():
    list_of_devices = subprocess.Popen("adb devices", shell=True, stdout=subprocess.PIPE).stdout.read()
    device_check = str(list_of_devices).replace("b'List of devices attached","")
    print(str(device_check))
    if "device" in str(device_check):
        print("------------------------------")
        print("Device is present.")
        print("You can proceed to choice 2.")
        print("------------------------------")
    else:
        print("------------------------------")
        print("No device is connected")
        print("Please connect your device")
        print("Activate USB Debugging from developer options")
        print("and then try again")
        print("------------------------------")
    main()


    
def download_tabs():
    list_of_devices = subprocess.Popen("adb devices", shell=True, stdout=subprocess.PIPE).stdout.read()
    if "device" in str(list_of_devices):
        print("Device is present.")
        print("Downloading opened tabs...")
        subprocess.Popen("adb forward tcp:9222 localabstract:chrome_devtools_remote", shell=True, stdout=subprocess.PIPE).stdout.read()
        json_file = "http://localhost:9222/json/list"
        file = wget.download(json_file)
        print("")
        print("The file has been downloaded")
        main()

def menu_display():
    print("1) Check if your mobile is connected")
    print("2) Download the opened tabs")
    print("3) Quit")
    print("Please select a choice 1,2 or 3:")
    menu_choice = input()
    return menu_choice

def main():
    choice = menu_display()
    while choice not in ["1","2","3"]:
        choice = menu_display()
    if choice == "1":
        devices_check()
    elif choice == "2":
        download_tabs()
    elif choice == "3":
        exit()

main()