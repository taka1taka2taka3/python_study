#リスト自体を逆順にする
python_list = []
python_list.append('python')
python_list.append('izm')
python_list.append('sample')
python_list.append('list')
python_list.append('reversed')

print('---------------------------------')
print('【そのまま表示】')
for value in python_list:
    print(value)

python_list.reverse()

print('---------------------------------')
print('【逆順表示】')
for value in python_list:
    print(value)



#リストの逆順結果を取得する
python_list = []
python_list.append('python')
python_list.append('izm')
python_list.append('sample')
python_list.append('list')
python_list.append('reversed')

print('---------------------------------')
print('【そのまま表示】')
for value in python_list:
    print(value)

print('---------------------------------')
print('【逆順表示】')
for value in reversed(python_list):
    print(value)

print('---------------------------------')
print('【リストの再表示】')
for value in python_list:
    print(value)



#スライスで逆順に取得する
python_list = []
python_list.append('python')
python_list.append('izm')
python_list.append('sample')
python_list.append('list')
python_list.append('reversed')

print('---------------------------------')
print('【そのまま表示】')
for value in python_list:
    print(value)

print('---------------------------------')
print('【逆順表示】')
for value in python_list[::-1]:
    print(value)

print('---------------------------------')
print('【リストの再表示】')
for value in python_list:
    print(value)
