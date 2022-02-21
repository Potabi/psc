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
commands_to_run=[]

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
        commands_to_run.append([args.psc_command.index(arg), is_command(arg),[]])
    else:
        if not commands_to_run:
            parser.print_help()
        else:
            commands_to_run[(len(commands_to_run)-1)][2].append(arg)

for command in commands_to_run:
    if command[1] == 'commit':
        for commit_command in commit(readmod(),command[2]):
            os.system(commit_command)
    if command[1] == "push":
        os.system(push(readmod(),command[2]))