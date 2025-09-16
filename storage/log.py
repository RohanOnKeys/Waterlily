import os

LOG_FILE = ".waterlily/log.lily"

def show_log():
    #Display commit history.

    
    if not os.path.exists(LOG_FILE):
        print("No log file found. Did you run 'init'?")
        return

    with open(LOG_FILE, "r") as log_file:
        lines = log_file.readlines()

    if not lines:
        print("No commits yet.")
        return

    print("Commit history:")
    for line in reversed(lines):  # newest commit first
        commit_id, *message = line.strip().split(" ", 1)
        print(f"{commit_id} - {message[0] if message else ''}")

