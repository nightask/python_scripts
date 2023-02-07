import os


# search file with key words
def search_file(search_path, key_word):
    if not os.path.isdir(search_path):
        print('查找的不是文件夹，退出')
        return

    for field_or_dir in os.listdir(search_path):
        path_join = os.path.join(search_path, field_or_dir)

        if os.path.isdir(path_join):
            search_file(path_join, key_word)

        elif key_word in os.path.basename(path_join):
            print(os.path.abspath(path_join))


if __name__ == '__main__':
    search_path = input('请录入要查找的目录：')
    key_word = input('请录入要查找的文件的关键字：')
    print('文件夹[', search_path, ']中包含[', key_word, ']关键字的文件列举如下：')
    search_file(search_path, key_word)