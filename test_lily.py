#This is the test part, we are running waterlily to create a test file with a hello message
#This then undergoes several commands to check if lily is doing her job



import os

def run(cmd):
    print(f"\n$ {cmd}")
    os.system(cmd)

def main():
    # 1. init repo
    run("python lily.py init")

    # 2. create a test file
    with open("hello.txt", "w") as f:
        f.write("Hello Waterlily!\n")
    print("Created hello.txt")

    # 3. add file
    run("python lily.py add hello.txt")

    # 4. commit file
    run("python lily.py commit 'first commit'")

    # 5. change file
    with open("hello.txt", "w") as f:
        f.write("Hello again!\n")
    print("Updated hello.txt")

    # 6. add + commit again
    run("python lily.py add hello.txt")
    run("python lily.py commit 'second commit'")

    # 7. log again
    run("python lily.py log")

    # 8. checkout first commit
    print("\nNow checking out the very first commit:")
    with open(".waterlily/log.lily") as f:
        first_commit = f.readline().split()[0]  # first line in log = oldest commit
        run(f"python lily.py checkout {first_commit}")

    # 9. show file contents after checkout
    with open("hello.txt") as f:
        print("hello.txt contents after checkout:", f.read().strip())

if __name__ == "__main__":
    main()
