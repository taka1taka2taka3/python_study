#XML-RPCクライアント

from datetime import datetime
from xmlrpc.client import ServerProxy


proxy = ServerProxy('http://localhost:8000/')

print(proxy.system.listMethods())
print(proxy.is_alive())
print(proxy.hello('World'))
nowtime = datetime.strptime(proxy.nowtime().value, '%Y%m%dT%H:%M:%S')
print(nowtime.strftime('%Y/%m/%d %H:%M:%S'))



#XML-RPCサーバー例

from datetime import datetime
from xmlrpc.client import DateTime
from xmlrpc.server import SimpleXMLRPCServer


def is_alive():
    return 'alive!'


def hello(message):
    return 'Hello {}.'.format(message)


def nowtime():
    return DateTime(datetime.now())


server = SimpleXMLRPCServer(('localhost', 8000))
print('Start Server')

server.register_function(is_alive, 'is_alive')
server.register_function(hello, 'hello')
server.register_function(nowtime, 'nowtime')

server.register_introspection_functions()

server.serve_forever()
