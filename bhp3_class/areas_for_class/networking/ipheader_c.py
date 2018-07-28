from ctypes import *
import os
import socket
import struct
import sys

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

class ICMP(Structure):
    _fields_ = [
        ("type",         c_ubyte),
        ("code",         c_ubyte),
        ("checksum",     c_ushort),
        ("unused",       c_ushort),
        ("next_hop_mtu", c_ushort)
    ]
    def __new__(self, socket_buffer):
        return self.from_buffer_copy(socket_buffer)

    def __init__(self, socket_buffer):
        pass

def sniff(host):
    socket_protocol = socket.IPPROTO_ICMP
    sniffer = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket_protocol)
    sniffer.bind((host, 0))
    sniffer.setsockopt(socket.SOL_IP, socket.IP_HDRINCL, 1)

    try:
        while True:
            raw_buffer = sniffer.recvfrom(65535)[0]
            ip_header = IP(raw_buffer[0:20])
            print('Protocol: %s %s -> %s' % (ip_header.protocol, ip_header.src_address, ip_header.dst_address))
            if ip_header.protocol == "ICMP":
                # calculate where our ICMP packet starts
                offset = ip_header.ihl * 4
                buf = raw_buffer[offset:offset + 8]
                icmp_header = ICMP(buf)
                print('ICMP -> Type: %s Code: %s' % (icmp_header.type, icmp_header.code))
                
    except KeyboardInterrupt:
        sys.exit()

if __name__ == '__main__':
    if len(sys.argv) == 2:
        host = sys.argv[1]
    else:
        host = '192.168.1.100'
    sniff(host)
