try:
    import requests
    import json 
    import time
    import colorama
    import os
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

                        created by hinick#5819
''')
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
    2: {Fore.CYAN}Preset Tags (Check Github for Tags){Fore.BLUE}
    3: {Fore.CYAN}Custom Tags{Fore.BLUE}
'''))

if choice == 1:
    url = "https://front35.omegle.com/start?caps=recaptcha2,t&firstevents=1&spid=&randid=PL83WE8G&topics=%5B%22discord%22%5D&lang=en"
if choice == 2:
    url = "https://front36.omegle.com/start?caps=recaptcha2,t&firstevents=1&spid=&randid=XX4XMCHK&topics=%5B%22dreamsmp%22%2C%22tommyinnit%22%2C%22dream%22%2C%22minecraft%22%2C%22fortnite%22%2C%22gaming%22%2C%22anime%22%2C%22manga%22%2C%22discord%22%2C%22twitter%22%2C%22quackity%22%2C%22sapnap%22%2C%22friends%22%2C%22furry%22%5D&lang=en"
if choice == 3:
    url = "https://front36.omegle.com/start?caps=recaptcha2,t&firstevents=1&spid=&randid=XX4XMCHK&topics=%5B"
    while True:
        tag = input(Fore.CYAN + "Please enter a tag (No Spaces): " + Fore.GREEN)
        if " " in tag:
            print(Fore.RED + "You cannot have spaces in your tag")
            continue
        if tag == "":
            url = url + "%5D&lang=en"
            url = url.replace("%2C%5D&lang=en", "%5D&lang=en")
            print("Tags set!" + Fore.BLUE)
            break
        print(tag)
        url += f"%22{tag}%22"
        url += "%2C"
if choice > 3:
    print("Invalid Choice")
    time.sleep(1)
    exit()
elif choice < 1:
    print("Invalid Choice")
    time.sleep(1)
    exit()
print("Checking JSON for Settings")
try:
    settings = open('settings.json')
except FileNotFoundError:
    print("json file was not found, make sure the settings.json file is there and in the same folder as this file.")
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
        if shard.startswith("central"):
            data = {'id': shard}
            check = requests.post("https://front8.omegle.com/events", data=data)
            print("connected to user, printing event response")
            #i would print the interests, however omegle sends them in nested arrays rather than json. and sometimes it responds with different things. 
            #so its much more safer to just print the response to the events endpoint.
            #if you'd like to deal with omegles shitty api and print pretty responses, you can do it yourself
            print("-----------------------------------")
            print(check.text)
            print("-----------------------------------")
            connect_to_chat(shard)
        else:
            print(Fore.RED + "An error occured when getting a shard. Make sure you set your interests correctly.")
            time.sleep(5)
            exit()
    getid()
