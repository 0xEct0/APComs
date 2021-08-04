# Att&ckCommands.py
# How to run:
#   
#   python3 Att&ckCommands.py [section] [OS]
#   Example: python3 Att&ckCommands.py recon
#       - User must put a section
#       - Operating system is optional (defaults to all)  
#
#   Available Sections:
#       - recon (reconnaissance)
#       - init (initial access) 
#   Available OS:
#       - Windows
#       - Linux
#       - Mac       



# imports
import sys
import json



# check if the user supplied correct number of arguments
# (name of file counts as argument)
if ((len(sys.argv) != 2) and (len(sys.argv) != 3)):
    print("\n**ERROR: Please provide the correct number of arguments")
    print("\nUsage: python3 Att&ckCommands.py [section] [OS (optional)]")
    print("Example 1: python3 Att&ckCommands.py recon")
    print("Example 2: python3 Att&ckCommands.py init windows")
    print("\nPossible sections:")
    print("\t[recon][init]")
    print("Possible OS:")
    print("\t[windows][linux][mac]")
    print("\tIf no argument is passed, default is all operating systems")
    exit()



# check if the argument is legitimate



# variables
recon_commands = "AttackReconnaissance.json"
file_to_open = ""
os_mode = ""



# get user commands/check if arguments are legitimate
if sys.argv[1] == "recon":
    file_to_open = "AttackReconnaissance.json"
elif sys.argv[1] == "init":
    file_to_open = "AttackInitialAccess.json"

if len(sys.argv) == 3:
    if sys.argv[2] == "Windows":
        os_mode = "Windows"
    elif sys.argv[2] == "Linux":
        os_mode = "Linux"
    elif sys.argv[2] == "Mac":
        os_mode = "Mac"
    else:
        quit()



# print welcome banner
print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
print("")
print("   _   _   _   ___        _      ___                                          _     ")             
print("  /_\ | |_| |_( _ )   ___| | __ / __\___  _ __ ___  _ __ ___   __ _ _ __   __| |___ ")
print(" //_\\\\| __| __/ _ \\/\\/ __| |/ // /  / _ \\| '_ ` _ \\| '_ ` _ \\ / _` | '_ \\ / _` / __|")
print("/  _  \ |_| || (_>  < (__|   </ /__| (_) | | | | | | | | | | | (_| | | | | (_| \__ \\")
print("\_/ \_/\__|\__\___/\/\___|_|\_\____/\___/|_| |_| |_|_| |_| |_|\__,_|_| |_|\__,_|___/")
print("")
print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
                                                                                  


# open/parse
f = open(file_to_open, 'r')

data = json.load(f)

for i in data['commands']: # eventually print out everything
    if os_mode in i['target OS']:
        print("****************************************")
        print("TITLE:\n" + i['title'] + "\n")
        print("DESCRIPTION:\n" + i['description'] + "\n")
        print("COMMAND:\n" + i['command'] + "\n")
        print("EXAMPLE:\n" + i['example'] + "\n")
        print("APPLICABLE OPERATING SYSTEMS:\n", end = "")
        print(*i['target OS'], sep = ", ")
        print("\nNOTES:\n" + i['notes'])
        print("****************************************\n")

f.close()