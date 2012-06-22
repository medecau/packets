from SocketServer import UDPServer
from SocketServer import BaseRequestHandler

__version__='0.0.0'
__author__='Pedro Rodrigues'

class BaseServer(UDPServer):
    """
        Local modification to UDPServer
    """
    def next(self):
        next = self.get_request()
        self.handle_request
        return next

class Server(object):
    """
        Interface to BaseServer()
    """
    def __init__(self, host='localhost', port=9999):
        self.server=BaseServer(("localhost", 9999), BaseRequestHandler)
        self.server.timeout = 0.1
    
    @property
    def next(self):
        return Packet(self.server.next())

class Packet(object):
    def __init__(self, s):
        self.s = s
        self.body = s[0][0]
        self.sock = s[0][1]
        self.addr = s[1]
    def reply(self, body):
        self.sock.sendto(body, self.addr)





