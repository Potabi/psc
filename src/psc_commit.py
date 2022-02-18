# psc commit . "message" push
# Add -> Commit -> Push
# Needs to use psc-push seperately

def commit(readmod, args):
    command_list=[]
    for commands in readmod:
        for command in commands:
            if command[0] == "add":
                command_list.append(command[1].replace("[arg]", args[0]))
            if command[0] == "commit":
                command_list.append(command[1].replace("[arg]", args[1]))
    return command_list
    