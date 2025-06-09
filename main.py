import os

def rename_readmes(base_path):
    for root, dirs, files in os.walk(base_path):
        for file in files:
            if file.lower() == "readme.md":
                folder_name = os.path.basename(root)
                old_path = os.path.join(root, file)
                new_path = os.path.join(root, f"{folder_name}.md")

                # Avoid overwriting existing files
                if os.path.exists(new_path):
                    print(f"Skipping: {new_path} already exists")
                else:
                    os.rename(old_path, new_path)
                    print(f"Renamed: {old_path} -> {new_path}")

# Change '.' to your starting directory
rename_readmes(".")
