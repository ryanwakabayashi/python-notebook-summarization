import os
import shutil

# Set the root directory where you want to remove all .ipynb files
root_directory = "C:/Users/ryanw/PycharmProjects/llama3-test/data/unzip-data"
#57,707 files in 0002

# Set the directory where you want to save all .ipynb files
destination_directory = "C:/Users/ryanw/PycharmProjects/llama3-test/data/all_ipynbs"
os.makedirs(destination_directory, exist_ok=True)  # Ensure the destination directory exists
print("Operation starting...")

for dirpath, dirnames, filenames in os.walk(root_directory):
    for file in filenames:
        file_path = os.path.join(dirpath, file)

        if file.endswith('.ipynb'):
            shutil.move(file_path, os.path.join(destination_directory, file))
        else:
            os.remove(file_path)

print('Operation complete.')
