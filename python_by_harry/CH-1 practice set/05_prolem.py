'''
Label the program written in problem 4 with comments.
'''
import os  # Import the built-in OS module for interacting with the file system

def print_directory_contents(path='.'):
    """
    Prints the contents of a directory.
    Default path is the current working directory ('.').
    """
    try:
        # Try to list all files and folders inside the given path
        contents = os.listdir(path)
    except FileNotFoundError:  # If the path doesn’t exist
        print(f"Error: Directory not found: {path}")
        return
    except NotADirectoryError:  # If the path is actually a file, not a directory
        print(f"Error: Not a directory: {path}")
        return
    except PermissionError:  # If the program doesn’t have permission to access the directory
        print(f"Error: Permission denied for directory: {path}")
        return

    # Print the directory name
    print(f"Contents of directory '{path}':")
    # Loop through each file/folder and print its name
    for name in contents:
        print(name)

if __name__ == '__main__':
    # Run the function with default path (current directory) 
    # You can replace '.' with any other directory path if needed
    print_directory_contents()
