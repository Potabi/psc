import argparse
import os
from psc_readmod import readmod 
from psc_clone import clone
from psc_commit import commit
from psc_push import push
from psc_pull import pull

parser = argparse.ArgumentParser()
parser.add_argument('psc_command', nargs='+', help='psc_command help')
args = parser.parse_args()

# Check commands
running=[]

def is_command(cmd):
    for commands in readmod():
        for command in commands:
            if cmd == command[0]:
                return cmd
                continue
            else:
                pass

for arg in args.psc_command:
    if is_command(arg):
        running.append([args.psc_command.index(arg), is_command(arg)])

print(running)