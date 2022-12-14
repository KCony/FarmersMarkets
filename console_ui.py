def print_ui(cmd, res):
    print(f'Your requested command was {cmd}')
    if cmd == 'list':
        print('The list of market names')
        for val in res:
            print(val)
    elif cmd == 'list cities':
        print('The list of all cities')
        for val in res:
            print(val)
    elif cmd == 'list cities ASC':
        print('The list of cities in alphabetical order')
        for val in res:
            print(val)
def get_command_prompt():
    return 'Input your command => '