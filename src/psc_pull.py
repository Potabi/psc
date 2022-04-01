def pull(readmod, args):
    for commands in readmod:
        for command in commands:
            if command[0] == "pull":
                arg_list = str()
                for arg in args:
                    arg_list = arg + " "
                return command[1].replace("[arg]", arg_list)