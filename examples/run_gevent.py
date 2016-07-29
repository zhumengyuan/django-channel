from gevent import monkey
monkey.patch_all()


import os
import sys
import getopt
import socket
from gevent.pywsgi import WSGIServer
from examples.wsgi import application

def get_listener(address):
    if address.startswith("unix"):
        address = address[5:]
        listener = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        if os.path.exists(address):
            os.remove(address)
        listener.bind(address)
        listener.listen(1)
    else:
        addr, port = address.split(":")
        listener = (addr, int(port))
    return listener

if __name__ == "__main__":
    listener = ('127.0.0.1', 18000)
    opts, _ = getopt.getopt(sys.argv[1:], "b:")
    for opt, value in opts:
        if opt == '-b':
            listener = get_listener(value)
    server = WSGIServer(listener, application, log=None, spawn=128)
    server.backlog = 64
    server.serve_forever()