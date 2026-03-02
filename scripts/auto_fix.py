import autopep8
import os
import sys

# Function to automatically fix common Python issues
def auto_fix_script(directory):
    # Walk through the directory structure
    for dirpath, _, filenames in os.walk(directory):
        for filename in filenames:
            if filename.endswith('.py'):
                file_path = os.path.join(dirpath, filename)
                fix_file(file_path)

# Function to fix individual file
def fix_file(file_path):
    try:
        # Read the file
        with open(file_path, 'r') as file:
            file_contents = file.read()

        # Auto-fix using autopep8
        fixed_contents = autopep8.fix_code(file_contents)

        # Write back the fixed code to the file
        with open(file_path, 'w') as file:
            file.write(fixed_contents)

        print(f"Fixed: {file_path}")
    except Exception as e:
        print(f"Error fixing {file_path}: {str(e)}")

if __name__ == '__main__':
    # Directory to fix
    auto_fix_script(sys.argv[1] if len(sys.argv) > 1 else '.')