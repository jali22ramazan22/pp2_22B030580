import os
lst = [1,2,3,4,5,6,7,8,9,10]
with open('main_dir/dir1/file2.txt', mode = "w") as file:
    file.write(str(lst) + "\n")
    file.close()
