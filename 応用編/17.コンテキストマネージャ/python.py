#特殊メソッドを実装する
class ContextManagerTest:

    def __enter__(self):
        print('__enter__')

    def __exit__(self, exc_type, exc_value, traceback):
        print('__exit__')


with ContextManagerTest():
    print('with')


    class ContextManagerTest:

        def __enter__(self):
            print('__enter__')

        def __exit__(self, exc_type, exc_value, traceback):
            print('__exit__')
            print(exc_type)
            print(exc_value)
            print(traceback)
            return True


    with ContextManagerTest():
        val = int('abc')


        class ContextManagerTest:

            def __enter__(self):
                print('__enter__')
                return 'as obj'

            def __exit__(self, exc_type, exc_value, traceback):
                print('__exit__')


        with ContextManagerTest() as as_obj:
            print(as_obj)



#デコレータを使用する
from contextlib import contextmanager


@contextmanager
def context_manager_test():
    print('enter')
    yield
    print('exit')


with context_manager_test():
    print('with')
