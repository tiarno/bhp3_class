from ctypes import *
import socket
import struct

class IP(Structure):
    _fields_ = [
        ("ihl",           c_ubyte,   4),
        ("version",       c_ubyte,   4),
        ("tos",           c_ubyte,   8),
        ("len",           c_ushort, 16),
        ("id",            c_ushort, 16),
        ("offset",        c_ushort, 16),
        ("ttl",           c_ubyte,   8),
        ("protocol_num",  c_ubyte,   8),
        ("sum",           c_ushort, 16),
        ("src",           c_uint32, 32),
        ("dst",           c_uint32, 32)
      ]
    def __new__(self, socket_buffer=None):
        return self.from_buffer_copy(socket_buffer)

    def __init__(self, socket_buffer=None):
        # human readable IP addresses
        self.src_address = socket.inet_ntoa(struct.pack("<L",self.src))
        self.dst_address = socket.inet_ntoa(struct.pack("<L",self.dst))

         # map protocol constants to their names
        self.protocol_map = {1: "ICMP", 6: "TCP", 17: "UDP"}
        try:
            self.protocol = self.protocol_map[self.protocol_num]
        except Exception as e:
            print(f'{e} No protocol for {self.protocol_num}')
            self.protocol = str(self.protocol_num)
