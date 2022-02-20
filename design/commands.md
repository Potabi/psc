> The Example Command:

```
psc commit . "Command Message" push
```

> Argument Parsing:

```
ARG: commit 
ARG: . 
ARG: "Command Message" 
ARG: push
```

> How it Works:
Treats every argument as an argument, checks if it is a command.
```
commands_to_run = [ ]
if it is a command:
    creates a sublist in commands_to_run(
        sublist[0]: Position of the command in the arguments,
        sublist[1]: The command name itself for later checks,
        sublist[2]: An empty sub-sublist for any arguments
    )
elif it is an argument:
    if there is no command in commands_to_run:
        display help information
        ends the script
    elif there are commands in commands_to_run:
        appends argument to sublist[2] of the last-appended command
```