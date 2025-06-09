import os

# Change this to your folder path
folder_path = "."

for filename in os.listdir(folder_path):
    # Check if filename starts with whitespace
    new_name = filename.lstrip()
    
    if new_name != filename:
        old_path = os.path.join(folder_path, filename)
        new_path = os.path.join(folder_path, new_name)
        
        os.rename(old_path, new_path)
        print(f"Renamed: '{filename}' -> '{new_name}'")
