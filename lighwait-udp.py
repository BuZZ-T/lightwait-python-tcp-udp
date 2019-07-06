#!/usr/bin/env python3

from __future__ import print_function
import sys
import re
from functools import reduce
import socket

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

def parse_color():
    if len(sys.argv) == 1:
        print('no color given!')
        sys.exit(1)

    color_string = sys.argv[1]

    if color_string in KNOWN_COLORS:
        send_color(KNOWN_COLORS[color_string])
    elif len(color_string) == 3:
        try: 
            color_index = [HEXMAP.index(c) for c in color_string.upper()]
            color = ':'.join([str(c*16+c) for c in color_index])
            send_color(color)
        except ValueError:
            print('three: not found')
    elif len(color_string) == 6:
        try: 
            color_index = [HEXMAP.index(c) for c in color_string.upper()]
            color_tuple = zip(*[iter(color_index)]*2)
            color = ':'.join([str(a*16 + b) for a,b in color_tuple])
            
            send_color(color)
        except ValueError:
            print('six: not found')
    else:
        print('no match: (%s): %s' % (len(color_string), color_string))


def send_color(color):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto(color.encode(), ('127.0.0.1', 3000))

if __name__ == '__main__':
    parse_color()
