import sys

def print_args(args):
    for item in args:
        print(item)

def check_flag(args):
    return ((args[1] == '-p') or (args[1] == '-i') or (args[1] == '-h') or (args[1] == '-w') or (args[1] == '-r'))

def flags(args):
    if(args[1] == '-p'):
        for item in args[2:]:
            print(item)
    elif(args[1] == '-i'):
        print("Hello World")
    elif(args[1] == '-h'):
        help_info = """Valid flags:
-p : prints out all the command line arguments after the -p
-i : prints "Hello World"
-h : prints out a help command"""
        print(help_info)
    elif(args[1] == '-w'):
        if len(args) == 3:
            print('No Content Provided')
            return
        output_file = open(args[2], 'w')
        for item in args[3:]:
            output_file.write(item + '\n')
        output_file.close()
    elif(args[1] == '-r'):
        input_file = open(args[2], 'r')
        for line in input_file:
            line = line.rstrip()
            print(line)
        input_file.close()
    return

def main():
    args = sys.argv
    if check_flag(args):
        flags(args)
    else:
        print_args(args)

if __name__ == "__main__":
    main()