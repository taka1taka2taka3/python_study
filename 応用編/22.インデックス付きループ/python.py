#インデックスと値を同時に取り出す
test_list = ['python', '-', 'izm', '.', 'com']

for idx, val in enumerate(test_list):
    print(idx, val)



#開始値を指定する場合は
test_list = ['python', '-', 'izm', '.', 'com']

for idx, val in enumerate(test_list, 1):
    print(idx, val)
