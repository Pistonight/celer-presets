import os
import sys

EXTENSIONS = ('.py', '.yaml', '.yml', '.md')


def convert_to_lf(directory):
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            if file_path.endswith(EXTENSIONS):
                with open(file_path, 'r', encoding='utf-8', newline='') as original_file:
                    content = original_file.read()
                    
                with open(file_path, 'w', encoding='utf-8', newline='\n') as converted_file:
                    converted_file.write(content)

if __name__ == "__main__":
    dir_path = sys.argv[1]
    convert_to_lf(dir_path)