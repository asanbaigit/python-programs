if __name__ == '__main__':
    L = []
    N = int(input())
    for i in range(N):
        command = ''
        t_command = input()
        l_command = t_command.split()
        if len(l_command) == 1:
                command = 'print(L)' if l_command[0] == 'print' else 'L.' + l_command[0] + '()'
        else:
            command = 'L.' + l_command[0] + '(' + ','.join(l_command[1:]) + ')'
        print(command)
        exec(command)