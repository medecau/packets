from SocketServer import UDPServer
from SocketServer import BaseRequestHandler
from random import randint

class BaseServer(UDPServer):
    """
        This is where we add/change functionality to UDPServer.
    """
    def next(self):
        next = self.get_request()
        return next

class User(object):
    """
        This wraps BaseServer with an interface for humans.
        
        Because we are all consenting adults,
        you still have lots of power!
        
        self.server gives you direct access to the BaseServer
        subclass and all its interesting funcionality.
        
        self.server.socket gives direct access to the socket
        
    """
    def __init__(self, host='localhost', port=9999):
        self.server=BaseServer((host, port), BaseRequestHandler)
        self.server.timeout = 0.1
    
    def sendto(self, addr, data):
        self.server.socket.sendto(data, addr)
    
    @property
    def next(self):
        return Packet(self.server.next())
    
    @property
    def addr(self):
        return self.server.socket.getsockname()
    
    @property
    def host(self):
        return self.addr[0]
    
    @property
    def port(self):
        return self.addr[1]

class Packet(object):
    def __init__(self, p=None):
        if p:
            self.package = p
            self.body = p[0][0].strip()
            self.sock = p[0][1]
            self.addr = p[1]
    
    def reply(self, body):
        self.sock.sendto(body, self.addr)
    
