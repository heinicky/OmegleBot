try:
    import requests
    import json 
    import time
    import colorama
    import os
    import urllib.parse
    from colorama import Fore
except ModuleNotFoundError:
    print("modules were not found, make sure you installed the correct modules")
except Exception as e:
    print(e)
colorama.init()
os.system("cls")
print(Fore.CYAN)
print('''
________                        .__           __________        __                      
\_____  \   _____   ____   ____ |  |   ____   \______   \ _____/  |_                    
 /   |   \ /     \_/ __ \ / ___\|  | _/ __ \   |    |  _//  _ \   __\                   
/    |    \  Y Y  \  ___// /_/  >  |_\  ___/   |    |   (  <_> )  |                     
\_______  /__|_|  /\___  >___  /|____/\___  >  |______  /\____/|__|                     
        \/      \/     \/_____/           \/          \/                                

                        created by heinick#0069
''')

print("this code sucks- nick")

print("If you want to use this program to advertise your server")
print('Format your invites to not include discord.gg/')
print("Example: Come on in!! --> BI9em0aQ")
print("This is just an example")
print("check my github to make sure you don't use any blacklisted words")
print(Fore.GREEN + "github.com/nickysayshi/OmegleBot" + Fore.CYAN)
print("------------------------------------------------------")
print("there is a JSON file in the same folder with the bot")
print("you can change the settings in there")
print("if the settings are left default, you will be asked to input them each time you run the bot")
print("So it is up to you to change them.")
print("------------------------------------------------------")
choice = int(input(f''' {Fore.BLUE}
which version would you like to use?
    1: {Fore.CYAN}Discord Tag Only{Fore.BLUE}
    2: {Fore.CYAN}Custom Tags{Fore.BLUE}
'''))

if choice == 1:
    url = 'https://front35.omegle.com/start?caps=recaptcha2,t&firstevents=1&spid=&randid=PL83WE8G&topics=%5B%22discord%22%5D&lang=en'
if choice == 2:
    tags = []
    while True:
        inp = input("Enter Your Tag (Press Enter to Finish): ")
        if " " in inp:
            print(Fore.RED + "You cannot have spaces in your tag" + Fore.BLUE)
            continue
        if inp == "":
            if len(tags) > 0:
                topics = urllib.parse.quote(str(tags).replace("'", '"'))
                url = f'https://front35.omegle.com/start?caps=recaptcha2,t&firstevents=1&spid=&randid=PL83WE8G&topics={topics}&lang=en'
                break
        else:
            tags.append(inp)
else:
    print("Invalid Choice")
    exit()

print("Checking JSON for Settings")
try:
    settings = open('settings.json')
except FileNotFoundError:
    print("JSON file was not found, make sure the settings.json file is there and in the same folder as this file.")
data = json.load(settings)
jsonmessage = data["message"]
jsontimer = data["timer"]

if jsonmessage == "None":
    print(f"{Fore.RED}No Message Found.{Fore.BLUE}")
    message = input("Enter Message: ")
else:
    message = jsonmessage
if jsontimer == 0:
    print(f"{Fore.RED}No Timer Found.{Fore.BLUE}")
    timer = int(input("Input Timer Between Messages (5 Seconds Recommended): "))
else:
    timer = jsontimer

i = 0
while True:
    r = requests.post(url)
    response = r.json()
    print("id obtained, connecting to a chat")
    print("-----------------------------------")
    
    def connect_to_chat(shard):

        global i

        message_data = {'msg': message, 'id': shard}

        message_endpoint = requests.post("https://front44.omegle.com/send", data=message_data)

        if message_endpoint.status_code == 200:
            print(f"sent {Fore.CYAN}{message}{Fore.BLUE}")
            i = i + 1
            print("-----------------------------------")
            print(f"Messages Sent: {Fore.CYAN}{i}{Fore.BLUE}")
            print("-----------------------------------")
        else:
            print(f"failed to send {message}")
            print("-----------------------------------")
        data = {'id': shard}
        disconnecting = requests.post("https://front8.omegle.com/disconnect", data=data)
        if disconnecting.status_code == 200:
            print("disconnected")
            print(f"sleeping for {timer} second(s)... ")
            time.sleep(timer)
            print("-----------------------------------")
        else:
            print("failed to disconnect")
        

    def getid():
        shard = response["clientID"]
        data = {'id': shard}
        check = requests.post("https://front8.omegle.com/events", data=data)
        json = check.json()
        print("connected to user, your common interests are:")
        print("-----------------------------------")
        try:
            interests = list(json[1][1])
            for interests in interests:
                print(Fore.GREEN + interests + Fore.BLUE)
            print("-----------------------------------")
        except:
            print("an unexpected response was found")
            print(json)
            return
            
        connect_to_chat(shard)

    getid()
