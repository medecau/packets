from json import loads
from random import randint
import socket
from SocketServer import UDPServer
from SocketServer import BaseRequestHandler

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
    def __init__(self, host='localhost', port=None):
        if port == None:
            port = randint(49152, 65535) # IANA ephemeral ports
            ephemeral = True
        else:
            ephemeral = False
        while True:
            try:
                self.server=BaseServer((host, port), BaseRequestHandler)
                break
            except socket.error, e:
                if ephemeral and e.errno == 48:
                    port = randint(49152, 65535) # IANA ephemeral ports
                else:
                    raise e
        self.server.timeout = 0.1
        self.server.allow_reuse_address = True
        self.server.request_queue_size = 5
    
    def sendto(self, addr, data):
        self.server.socket.sendto(data, addr)
    
    @property
    def next(self):
        return Packet(self.server.next(), self)
    
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
    """
        UDP packet wrapper.
        
        It's a wrapper that still gives you access to everything.
        
        self.packet is the original package
        
        and allows for simple replies with self.reply()
    """
    def __init__(self, packet, user):
        self.packet = packet
        self.user = user
    
    def reply(self, data):
        self.user.sendto(self.addr, data)
    
    @property
    def body(self):
        return self.packet[0][0].strip()

    @property
    def json(self):
        return loads(self.body)
    
    @property
    def sock(self):
        return self.packet[0][1]
    
    @property
    def addr(self):
        return self.packet[1]
    
    
