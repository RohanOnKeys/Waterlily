
import os
import shutil

STAGE_DIR = ".waterlily/stage"

def add_file(file_path):
    #Add a file to stage
    if not os.path.exists(file_path):
        print(f"File '{file_path}' does not exist.")
        return

    os.makedirs(STAGE_DIR, exist_ok=True)

    # copy file into stage
    filename = os.path.basename(file_path)
    shutil.copy2(file_path, os.path.join(STAGE_DIR, filename))
    print(f"Added '{filename}' to staging area.")

def remove_file(file_path):
    """Remove a file from the staging area."""
    filename = os.path.basename(file_path)
    staged_file = os.path.join(STAGE_DIR, filename)

    if os.path.exists(staged_file):
        os.remove(staged_file)
        print(f"Removed '{filename}' from staging area.")
    else:
        print(f"File '{filename}' not found in staging area.")
