import os
from pathlib import Path

def get_file_contents(root_dir):
    result = {}
    for dirpath, dirnames, filenames in os.walk(root_dir):
        # Exclude the 'env' directory
        if 'env' in dirnames:
            dirnames.remove('env')
        
        for filename in filenames:
            file_path = Path(dirpath) / filename
            # Skip if the path points to the 'env' directory
            if 'env' in file_path.parts:
                continue
            
            try:
                with open(file_path, 'r', encoding='utf-8') as file:
                    content = file.read()
                    result[str(file_path)] = content
            except Exception as e:
                print(f"Error reading {file_path}: {e}")
    
    return result

if __name__ == "__main__":
    # Set the root directory to the current working directory
    root_directory = Path.cwd()
    files_content = get_file_contents(root_directory)
    
    # Print the file paths and their contents
    for file_path, content in files_content.items():
        print(f"File Path: {file_path}")
        print("Content:")
        print(content)
        print("-" * 50)