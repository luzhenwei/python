import os




"""
获取指定路径下的文件名
"""
def all_files_path(rootDir):
    for root, dirs, files in os.walk(rootDir):     # 分别代表根目录、文件夹、文件
        for file in files:                         # 遍历文件
            file_path = os.path.join(root, file)   # 获取文件绝对路径
            filepaths.append(file_path)            # 将文件路径添加进列表
        for dir in dirs:                           # 遍历目录下的子目录
            dir_path = os.path.join(root, dir)     # 获取子目录路径
            all_files_path(dir_path)               # 递归调用





if __name__ == "__main__":
    filepaths = []                                 # 初始化列表用来
    all_files_path(r'G:\office')
    for filepath in filepaths:
        print(filepath)
    # with open('dir.txt', 'a') as f:
    # 	for filepath in filepaths:
    # 		f.write(filepath + '\n')
