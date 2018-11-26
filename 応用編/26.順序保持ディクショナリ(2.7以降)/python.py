#collections.OrderedDict
test_dict = {}

test_dict['word'] = 'doc'
test_dict['excel'] = 'xls'
test_dict['access'] = 'mdb'
test_dict['powerpoint'] = 'ppt'
test_dict['notepad'] = 'txt'
test_dict['python'] = 'py'

for key in test_dict:
    print(key)


import collections

test_dict = collections.OrderedDict()

test_dict['word'] = 'doc'
test_dict['excel'] = 'xls'
test_dict['access'] = 'mdb'
test_dict['powerpoint'] = 'ppt'
test_dict['notepad'] = 'txt'
test_dict['python'] = 'py'

for key in test_dict:
    print(key)
