#ファイル、ディレクトリの存在チェック
import os

filepath = 'c:/python'

if os.path.exists(filepath):
    print('指定のファイル、またはディレクトリが存在しています。')

    if os.path.isfile(filepath):
        print('指定のパスはファイルです。')

    if os.path.isdir(filepath):
        print('指定のパスはディレクトリです。')

else:
    print('指定のファイル、またはディレクトリが存在していません。')



#ディレクトリの作成と削除
import os
import shutil

def show_dir(path):
    print('====================================')
    for dirpath, dirnames, filenames in os.walk(path):
        for dirname in dirnames:
            print(os.path.join(dirpath, dirname))


tmpdir = 'c:/python/tmp'

os.mkdir(tmpdir)
os.makedirs('c:/python/tmp/mkdir1/mkdir2/mkdir3')
show_dir(tmpdir)

os.rmdir('c:/python/tmp/mkdir1/mkdir2/mkdir3')
show_dir(tmpdir)

# os.removedirs(tmpdir)
shutil.rmtree(tmpdir)



#ファイル、ディレクトリのコピー
import os
import shutil

shutil.copy('c:/python/src.txt', 'c:/python/dest.txt')
shutil.copytree('c:/python', 'c:/python_backup')
