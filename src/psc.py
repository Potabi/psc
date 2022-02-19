import sys
import os
from psc_readmod import readmod 
from psc_clone import clone
from psc_commit import commit
from psc_push import push
from psc_pull import pull

args = []
for arg in sys.argv:
    if sys.argv.index(arg) < 2:
        pass
    else:
        args.append(arg)
    
def checkcommand(readmod,args,position):
    # for i in base_commands:
    #     if (str(command) == str(i)):
    #         scmrun(str(i),int(position))
    #     else:
    #         exit

    for commands in readmod:
        for command in commands:
            for arg in args:
                if command[0] == arg:
                    args.pop(0)
                    run_command(readmod,arg,args,position)
                else:
                    pass

def run_command(readmod,arg,args,position):
    
    if len(sys.argv) < int(position):
        exit
    else:
        print(commit(readmod,args))

    # If there are any other arguments
    if len(sys.argv) >= 5:
        checkcommand(str(sys.argv[4]),int(4))

checkcommand(readmod(),sys.argv,int(1))