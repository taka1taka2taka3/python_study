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
