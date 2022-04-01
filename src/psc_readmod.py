# Default: /etc/psc
# In-dev: ./configs/mods.psc
mods_location = "/etc/psc/mods.psc" 
mods_directory = "/etc/psc/"
mods_commands = []
mods_file = []
mods_functions = []

def readmod():
    with open(mods_location, "r") as mods_list:
        mods = mods_list.readlines()
        for mod in mods:
            mod = mod.split("=")
            mods_commands.append(str(mod[0]))
            mods_file.append(mods_directory + str(mod[1]))

    functions_list = []
    for mod_file in mods_file:
        with open(mod_file, "r") as mod_command_list:
            for line in mod_command_list.readlines():
                line = line.split("=")
                line[1] = line[1].replace("\n","")
                functions_list.append(line)
            mods_functions.append(functions_list)
        functions_list = []
    return mods_functions