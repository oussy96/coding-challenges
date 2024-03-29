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


def get_parse_filename(args):
    return args.filename


def get_input():
    return sys.stdin


def get_filepath(filename):
    return os.path.join(os.getcwd(), filename)


def cat_file(filename):
    try:
        # Open the file in read mode ('r')
        with open(filename, 'r') as file:
            # Read all lines into a list
            lines = file.readlines()

        # Print each line
        for line in lines:
            print(line.strip())  # .strip() removes trailing newline characters
    except FileNotFoundError:
        print(f"Error: {filename} not found")


def cat_input(stdin_):
    for line in stdin_:
        print(line.strip())


def cat_input_nb_lines(stdin_):
    n = 1
    for line in stdin_:
        print(f'{n} {line.strip()}')
        n += 1

    
def cat_input_nb_exc_nb_lines(stdin_):
    n = 1
    for line in stdin_:
        if line == '\n':
            print(line.strip())
        else:
            print(f"{n} {line.strip()}")
            n = n + 1 

def cat_argument(args):
    if args.filename:
        file_arg = get_parse_filename(args)
        for file in file_arg:
            cat_file(get_filepath(file))
    elif args.read:
        stdin_ = get_input()
        cat_input(stdin_)
    elif args.number:
        stdin_ = get_input()
        cat_input_nb_lines(stdin_)
    elif args.bnumber:
        stdin_ = get_input()
        cat_input_nb_exc_nb_lines(stdin_)


if __name__ == "__main__":
    # Build the files path
    args = set_parse_commands()
    cat_argument(args)

