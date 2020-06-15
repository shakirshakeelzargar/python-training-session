import os
def directory_list(path):
    for (root,dirs,files) in os.walk(path, topdown=True): 
        print(root) 
        print (dirs) 
        print (files) 
        print('-'*60)
path=f"D:{os.sep}DDFTQA"
directory_list(path)

#2.

for root, dirs, files in os.walk(path, topdown=True):
    for dir_name in dirs:
      print(os.path.join(root, dir_name))
    for file_name in files:
      print(os.path.join(root, file_name))
    print("-"*60)
#3.
def root_directory_list():
    '''
    getting directory list using next() and walk() function
    '''
    #only root directory
    root=next(os.walk(path))[0]
    print(f"root directory : {root}")
    #directory list
    dirs=next(os.walk(path))[1]
    print(f"directory list: {dirs}")
    #files list
    files=next(os.walk(path))[2]
    print(f"files list : {files}")
root_directory_list()