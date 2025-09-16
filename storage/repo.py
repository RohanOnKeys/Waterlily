#For the empty stage and commits dir
import os
#For the  commits, encryption into SHA1 and other commit funtions
import hashlib
import time
import shutil




def init_repo():
    os.makedirs(".waterlily/stage", exist_ok=True)
    os.makedirs(".waterlily/commits", exist_ok=True)

    # create an empty log + head, write mode
    open(".waterlily/log.lily", "w").close()
    with open(".waterlily/HEAD", "w") as f:
        f.write("")  
        # empty HEAD initially

    print("Initialized empty Waterlily repository.")



def commit_changes(message):
    stage_dir = ".waterlily/stage"
    commits_dir = ".waterlily/commits"

    # if no staged files
    if not os.listdir(stage_dir):
        print("No files staged for commit.")
        return

    #Generates a commit ID (hash of message + timestamp)
    timestamp = str(time.time())
    commit_id = hashlib.sha1((message + timestamp).encode()).hexdigest()[:7]

    commit_path = os.path.join(commits_dir, commit_id)
    os.makedirs(commit_path, exist_ok=True)

    #Moves all files from stage/ → .waterlily/commits/<commit_id>/.
    for filename in os.listdir(stage_dir):
        src = os.path.join(stage_dir, filename)
        dst = os.path.join(commit_path, filename)
        shutil.copy2(src, dst)

    # append log entry to log.lily
    with open(".waterlily/log.lily", "a") as log_file:
        log_file.write(f"{commit_id} {message}\n")

    # updates HEAD to a new HEAD
    with open(".waterlily/HEAD", "w") as head_file:
        head_file.write(commit_id)

    # clear stage area after commit
    for filename in os.listdir(stage_dir):
        os.remove(os.path.join(stage_dir, filename))

    print(f"Committed as {commit_id}: {message}")
