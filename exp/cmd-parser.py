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

cmdparse_arg=[]
cmdparse_cmd=[]
for i in cmdparse:
    if i[0] == "cmd":
        cmdparse_cmd.append(i)
    elif i[0] == "arg":
        cmdparse_arg.append(i) 
# print(cmdparse,"\n"+str(cmdparse_arg),"\n"+str(cmdparse_cmd))

for i in cmdparse_cmd:
    for x in cmdparse_arg:
        if x[1] > i[1]:
            print(i,x[2])