import os
import shutil

COMMITS_DIR = ".waterlily/commits"
HEAD_FILE = ".waterlily/HEAD"

def checkout_commit(commit_id):
    #Restore files from a previous commit into the working directory.

    commit_path = os.path.join(COMMITS_DIR, commit_id)

    if not os.path.exists(commit_path):
        print(f"Commit '{commit_id}' does not exist.")
        return

    # copy files from commit into working dir
    for filename in os.listdir(commit_path):
        src = os.path.join(commit_path, filename)
        dst = os.path.join(".", filename)  
        
        # overwrite in working dir
        shutil.copy2(src, dst)

    # update HEAD
    with open(HEAD_FILE, "w") as head_file:
        head_file.write(commit_id)

    print(f"Checked out commit {commit_id}.")

