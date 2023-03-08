import os
path = 'main_dir/dir1/file1.txt'
with open(path) as file:
    print(f"The count of lines in {path} is {len(file.readlines())}")
    file.close()