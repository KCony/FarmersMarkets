"""
Console UI
"""


def print_ui(cmd, res):
    """docstring"""
    print(f'Your requested command was {cmd}')
    if (type(cmd) is list) and (len(cmd) > 1):
        if cmd[0] == 'list':
            print('The list of market names')
            for val in res:
                print(val)
    # elif (type(cmd) is list) and (cmd[0] == 'list'):
    #     print('The list of market names')
    #     for val in res:
    #         print(val)
    else:
        print("List of available commands: ", res)


def get_command_prompt():
    """pass"""
    return 'Input your command => '


def get_arguments_prompt(command):
    """pass"""
    return 'Input additional arguments for command ' + command + ' => '
