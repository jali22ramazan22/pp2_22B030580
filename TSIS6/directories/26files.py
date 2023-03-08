import os

path = "main_dir/26directory/"
for i in range(26):
    file = open(path + f"file{chr(i+65)}.txt", "w+")
    file.close()
