#ファイルの読み込み
f = open('read.txt', 'r')

for row in f:
    print(row)

f.close()



#ファイルに書き込み
f = open('write.txt', 'w')

f.write('Pythonでファイルに書き込みました！')

f.close()
