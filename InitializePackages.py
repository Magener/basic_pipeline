import os

def add_init_files(directory):
    for dirpath, dirnames, filenames in os.walk(directory):
        if any(filename.endswith('.py') for filename in filenames):
            init_file = os.path.join(dirpath, '__init__.py')
            if not os.path.isfile(init_file):
                with open(init_file, 'w') as file:
                    pass  # Create an empty __init__.py file

if __name__ == "__main__":
    target_directory = "."  # Replace this with your target directory
    add_init_files(target_directory)