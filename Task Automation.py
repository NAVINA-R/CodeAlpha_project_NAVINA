import os
import shutil

def organize_files_by_type(directory):
    # Get a list of all files in the directory
    files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
    
    for file in files:
        # Extract the file extension
        file_extension = os.path.splitext(file)[1][1:]  # Exclude the dot
        
        if not file_extension:
            file_extension = 'no_extension'
        
        # Create the target directory if it doesn't exist
        target_directory = os.path.join(directory, file_extension)
        if not os.path.exists(target_directory):
            os.makedirs(target_directory)
        
        # Move the file to the target directory
        src_path = os.path.join(directory, file)
        dst_path = os.path.join(target_directory, file)
        shutil.move(src_path, dst_path)
        print(f"Moved: {src_path} -> {dst_path}")

if __name__ == "__main__":
    # Specify the directory to organize
    target_directory = "path_to_your_directory"
    organize_files_by_type(target_directory)
