import os

ret_tuple = os.walk('..', topdown=True)
print(ret_tuple)

for cur_dir, list_dir, list_file in ret_tuple:
    print('当前目录：', cur_dir)

    if len(list_dir) > 0:
        print('包含的子目录：', list_dir)
    if len(list_file) > 0:
        print('当前目录下的文件：', list_file)

    print('******')