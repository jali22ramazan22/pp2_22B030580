import os
path = 'main_dir/dir2/file3.txt'

if os.path.exists(path):
    os.remove(path)
else:
    print('File does not exist')

