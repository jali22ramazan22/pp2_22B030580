import os

path = 'main_dir/dir1/file1.txt'
file = str()
if os.path.exists(path):
    for i in range(14, len(path)):
        file += path[i]
    print(f"The file '{file}' exists")
else:
    print("Written path is not valid")