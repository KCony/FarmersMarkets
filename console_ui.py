def print_ui(cmd, res):
    # print(f'Your requested command was {cmd}')
    if cmd == 'error':
        print("List of available commands: ", res)  # Если передается команда, не входящая в список доступных
    if (cmd is not None) and len(cmd) == 1:  # Если это команда list без аргументов
     if cmd[0] == 'list':   # Если передали команду list
        print('The list of market names')
        for val in res: print(val)
    if (len(cmd) > 1) and (cmd[0] == 'find'):  # find передается список и команда требует дополнительных аргументов
        print("Command: ", cmd)
    if (len(cmd) > 1) and (cmd[0] == 'list'):  # find передается список и команда требует дополнительных аргументов
        print("Command: ", cmd)


def get_command_prompt():
    return 'Input your command => '

def get_arguments_prompt(command):
    return 'Input additional arguments for command ' + command + ': '