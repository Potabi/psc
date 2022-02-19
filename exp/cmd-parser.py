import sys

cmd_list=["clone","commit","pull","push"]

# [TYPE,POS,ARG]
cmdparse=[]

print(str(sys.argv))
sys.argv.pop(0)
for i in sys.argv:
    if i in cmd_list:
        cmdparse.append(["cmd",sys.argv.index(i),i])
    else:
        cmdparse.append(["arg",sys.argv.index(i),i])

print(cmdparse)