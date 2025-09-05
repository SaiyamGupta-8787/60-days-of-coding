import os

def print_directory_contents(path='.'):
    try:
        contents = os.listdir(path)
    except FileNotFoundError:
        print(f"Error: Directory not found: {path}")
        return
    except NotADirectoryError:
        print(f"Error: Not a directory: {path}")
        return
    except PermissionError:
        print(f"Error: Permission denied for directory: {path}")
        return

    print(f"Contents of directory '{path}':")
    for name in contents:
        print(name)

if __name__ == '__main__':
    # Use the current directory or replace with a custom path
    print_directory_contents()