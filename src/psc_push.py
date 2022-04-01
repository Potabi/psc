from distutils.spawn import spawn


def push(readmod, args):
    for commands in readmod:
        for command in commands:
            if command[0] == "push":
                arg_list = str()
                for arg in args:
                    arg_list = arg_list + arg + " "
                return command[1].replace("[arg]", arg_list)