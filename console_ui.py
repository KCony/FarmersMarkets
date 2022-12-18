def print_ui(cmd, res):
    print(f'Your requested command was {cmd}')
    if (type(cmd) is list) and (len(cmd) > 1):  # Если команда требует дополнительных аргументов
     if cmd[0] == 'list':
        print('The list of market names')
        for val in res:
            print(val)
    elif (type(cmd) is list) and (cmd[0] == 'list'):
        print('The list of market names')
        for val in res:
            print(val)
    else: print("List of available commands: ", res)

def get_command_prompt():
    return 'Input your command => '