#ジェネレータ関数 – yield
def func_sample():
    print('おはよう')
    print('こんにちは')
    print('こんばんは')

func_sample()


def func_sample():
    yield('おはよう')
    yield('こんにちは')
    yield('こんばんは')

for i in func_sample():
    print(i)


def func_sample():
    yield('おはよう')
    yield('こんにちは')
    yield('こんばんは')

f = func_sample()
print(next(f))
print(next(f))
print(next(f))



#ジェネレータ式
gen_sample = (i for i in 'おはよう こんにちは こんばんは'.split())

print(gen_sample)
for i in gen_sample:
    print(i)
