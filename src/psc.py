import sys
import os
from psc_readmod import readmod 
from psc_clone import clone
from psc_commit import commit
from psc_push import push
from psc_pull import pull

command = sys.argv[1]

# Sets the list of arguments
args = []
for arg in sys.argv:
    if sys.argv.index(arg) < 2:
        pass
    else:
        args.append(arg)

if command == "clone":
    os.system(clone(readmod(), args))
if command == "commit":
    for command in commit(readmod(), args):
        os.system(command)
    for arg in args:
        if arg == "push":
            os.system(push())
if command == "push":
    os.system(push(readmod(), args))
if command == "pull":
    os.system(pull(readmod(), args))