import sys

cmd_list=["clone","commit","pull","push"]

print(str(sys.argv))
sys.argv.pop(0)
for i in sys.argv:
    if i in cmd_list:
        print("cmd: ",sys.argv.index(i),i)
    else:
        print("arg: ",sys.argv.index(i),i)
