import argparse
import os
from psc_readmod import readmod 
from psc_clone import clone
from psc_commit import commit
from psc_push import push
from psc_pull import pull

parser = argparse.ArgumentParser()
parser.add_argument('bar', nargs='+', help='bar help')
args = parser.parse_args()

# Check commands
for commands in readmod():
    for command in commands:
        print(command)
        if args.bar[0] == command[0]:
            print(args.bar[0])