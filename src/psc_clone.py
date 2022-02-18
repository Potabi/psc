def clone(readmod, args):
    for commands in readmod:
        for command in commands:
            if command[0] == "clone":
                min_args = 1
                if len(args) < min_args:
                    print("Err: Too Few Arguments")
                    print("Usage: psc clone []")

                arg_list = ""
                for arg in args:
                    arg_list = arg_list + arg + " "
                clone_command = command[1].replace("[arg]", arg_list)
                return clone_command