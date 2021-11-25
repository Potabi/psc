#!/bin/python3
import sys
import os
# If debugging is ever needed: 
# print('Number of arguments:', len(sys.argv), 'arguments.')
# print('Argument List:', str(sys.argv))

base_commands=["clone","pull","commit","push"]

# psc commit <dir> "message" push
if len(sys.argv) < 2:
    exit

# Check if command is valid
def checkcommand(command,position):
    for i in base_commands:
        if (str(command) == str(i)):
            scmrun(str(i),int(position))
        else:
            exit

def scmrun(command,position):
    if(command == "commit"):
        if len(sys.argv) < 4 or len(sys.argv) > 5:
            exit
        else:
            directory = sys.argv[int(int(position)+1)]
            message   = sys.argv[int(int(position)+2)]

            print("Committing `" + str(directory) + "` with message `" + str(message) + "`")
            os.system("git add " + str(directory))
            os.system("git commit -m \"" + str(message) + "\"")

        if len(sys.argv) == 5:
            checkcommand(str(sys.argv[4]),int(4))
    elif(command == "clone"):
        pass
    elif(command == "pull"):
        pass
    elif(command == "push"):
        os.system("git push")
        

checkcommand(str(sys.argv[1]),int(1))