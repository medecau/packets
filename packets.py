from SocketServer import UDPServer
from SocketServer import BaseRequestHandler
from random import randint

class BaseServer(UDPServer):
    """
        Local modification to UDPServer
    """
    def next(self):
        next = self.get_request()
        self.handle_request
        return next

class User(object):
    """
        Interface to BaseServer()
    """
    def __init__(self, host='localhost', port=9999):
        self.server=BaseServer((host, port), BaseRequestHandler)
        self.server.timeout = 0.1
        self.addr = self.server.socket.getsockname()
        self.host, self.port = self.addr
    
    def sendto(self, addr, data):
        self.server.socket.sendto(data, addr)
    
    @property
    def next(self):
        return Packet(self.server.next())

class Packet(object):
    def __init__(self, p=None):
        if p:
            self.package = p
            self.body = p[0][0].strip()
            self.sock = p[0][1]
            self.addr = p[1]
    
    def reply(self, body):
        self.sock.sendto(body, self.addr)
    
