import os
import argparse
import sys


def set_parse_commands():
    # Create ArgumentParser object
    parser = argparse.ArgumentParser(prog='cccat', description='Process cat file.')

    # Create mutually exclusive group for filename and input
    # group = parser.add_mutually_exclusive_group()

    # Add arguments
    parser.add_argument('filename', type=str, nargs='*'
                       , help='The name of file to display his content')
    parser.add_argument('-', '--read', action='store_true', 
                        help='Read the input from standard in')
    parser.add_argument('-n', '--number', action='store_true'
                       , help='Number the lines printed out including non-blank lines')
    parser.add_argument('-b', '--bnumber', action='store_true'
                       , help='Number the lines printed out excluding non-blank lines')
    
    # Parse the arguments
    args = parser.parse_args()
    
    return args


def get_stdin():
    # print(sys.stdin.read())
    return sys.stdin


def get_filepath(filename):
    return os.path.join(os.getcwd(), filename)


def read_file(filename):
    result = ''
    try:
        # Open the file in read mode ('r')
        with open(filename, 'r') as file:
            # Read all lines into a list
            lines = file.readlines()

        # Print each line
        for line in lines:
            result += line
        
        return result
    except FileNotFoundError:
        print(f"Error: {filename} not found")


def read_input(stdin_):
    result = ''
    for line in stdin_:
        result += line.strip()
    return result

def read_input_nb_lines(stdin_):
    result = ''
    n = 1
    for line in stdin_:
        result += f'{n}{line}' if line == '\n' else f'{n} {line}' 
        n += 1
    return result

    
def read_input_nb_exc_nb_lines(stdin_):
    result = ''
    n = 1
    for line in stdin_:
        if line == '\n':
            result += line
        else:
            result += f"{n} {line}"
            n = n + 1 
    return result


def cc_cat(args):
    if args.filename:
        result = ''
        for file in args.filename:
            result += read_file(get_filepath(file))
        return result
    elif args.read:
        return read_input(get_stdin())
    elif args.number:
        return read_input_nb_lines(get_stdin())
    elif args.bnumber:
        return read_input_nb_exc_nb_lines(get_stdin())


if __name__ == "__main__":
    # Build the files path
    args = set_parse_commands()
    print(cc_cat(args))
