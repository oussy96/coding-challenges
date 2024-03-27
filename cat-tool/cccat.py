import os
import sys

def get_filename():
    if len(sys.argv) != 2:
        print("Usage: cccat <filename>")
        sys.exit(1)
    
    return sys.argv[1]


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


if __name__ == "__main__":
    # Build the files path
    filepath = os.path.join(os.getcwd(), get_filename())
    
    cat_file(filepath)
