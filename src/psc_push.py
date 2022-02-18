def push(readmod, args):
    for commands in readmod:
        for command in commands:
            if command[0] == "push":
                arg_list = ""
                for arg in args:
                    arg_list = arg + " "
                return command[1].replace("[arg]", arg_list)