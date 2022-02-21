def commit(readmod,args):
    command_list=[]
    for commands in readmod:
        for command in commands:
            if command[0] == "commit":
                if command[1].replace("[arg]", args[1]) in command_list:
                    pass
                else:
                    command_list.append(command[1].replace("[arg]", args[1]))
            if command[0] == "add":
                if command[1].replace("[arg]", args[0]) in command_list:
                    pass
                else:
                    command_list.append(command[1].replace("[arg]", args[0]))
    return command_list
    