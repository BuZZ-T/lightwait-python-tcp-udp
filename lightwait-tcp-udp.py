#!/usr/bin/env python3

from __future__ import print_function
import enum
import sys
import re
from functools import reduce
import socket

HOST = 'localhost'
PORT = 3030

KNOWN_COLORS = {
    'black': '0:0:0',
    'white': '255:255:255',
    'red': '255:0:0',
    'yellow': '255:255:0',
    'green': '0:255:0',
    'blue': '0:0:255',
    'magenta': '255:0:255',
    'cyan': '0:255:255',
    'off': '0:0:0'
}

HEXMAP = '0123456789ABCDEF'

class Protocol(enum.Enum):
    TCP = 'TCP'
    UDP = 'UDP'


# available: TCP, UDP
used_protocol = Protocol.UDP

class LightwaitTcpUdp(object):

    tcp_sock = None

    def __setup_tcp(self):
        self.tcp_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.tcp_sock.connect((HOST, PORT))
        except Exception:
            print('Connection refused for TCP port %s on "%s"!. Maybe the presenter is not started?' % (PORT, HOST))
            return

    def __init__(self, protocol: Protocol):
        self.protocol = protocol
        if protocol == Protocol.TCP:
            self.__setup_tcp()

    def __del__(self):
        if self.tcp_sock:
            self.tcp_sock.close()

    def __send_color_udp(self, color):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            sock.sendto(color.encode(), (HOST, PORT))
        except Exception as e:
            print('Failed to send UDP message', e)

    def __send_color_tcp(self, color):
        try:
            self.tcp_sock.sendall(color.encode())
        except Exception as e:
            print('failed to send TCP message', e)
        # finally:
        #     sock.close()

    def send(self, blink: bool, color: str):
        color_to_send = ('b' if blink else '') + color
        if self.protocol == Protocol.TCP:
            self.__send_color_tcp(color_to_send)
        elif self.protocol == Protocol.UDP:
            self.__send_color_udp(color_to_send)
        else:
            print('Unknown protocol "%s", only "TCP" and "UDP" are currently supported!')


def parse_color(color_string):
    if color_string in KNOWN_COLORS:
        return KNOWN_COLORS[color_string]
    elif len(color_string) == 3:
        try:
            color_index = [HEXMAP.index(c) for c in color_string.upper()]
            color = ':'.join([str(c*16+c) for c in color_index])
            return color
        except ValueError:
            return None
    elif len(color_string) == 6:
        try:
            color_index = [HEXMAP.index(c) for c in color_string.upper()]
            color_tuple = zip(*[iter(color_index)]*2)
            color = ':'.join([str(a*16 + b) for a, b in color_tuple])
            return color
        except ValueError:
            return None
    else:
        return None


def main():
    global used_protocol

    if len(sys.argv) == 1:
        print('no color given!')
        sys.exit(1)

    # TODO: move parse logic into lw.send

    blink_flag_set = sys.argv[1] == '--blink' or sys.argv[1] == '-b'
    blink_mode = blink_flag_set or len(sys.argv) > 2

    color_strings = sys.argv[2:] if blink_flag_set else sys.argv[1:]
    parsed_colors = [parse_color(color) for color in color_strings if color is not None]
    colors = [color for color in parsed_colors if color is not None]

    # program name without path
    program_name = sys.argv[0].split('/')[-1]

    # overwrite protocol by name of program (use "ln -s" for that!)
    if not 'tcp' in program_name and 'udp' in program_name:
        used_protocol = Protocol.UDP
    elif 'tcp' in program_name and not 'udp' in program_name:
        used_protocol = Protocol.TCP

    lw_tcp_udp = LightwaitTcpUdp(used_protocol)
    lw_tcp_udp.send(blink_mode, '|'.join(colors))


if __name__ == '__main__':
    main()
