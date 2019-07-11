# lightwait-python-udp

This is a transmitter for UDP-based presenters in the [lightwait-stack](https://github.com/BuZZ-T/lightwait).

## Features

* Written in a few lines of python (~70)
* Supports multiple formats as input
    * known color names ("white", "black", "red", ...) See full list: TODO
    * case-insensitive 3-digit hex code without the leading # (e.g. "F00", meaning "#FF0000")
    * case-insensitive 6-digit hex code without the leading # (e.g. "FF0000")
* Supports
    * solid color
    * blinking color (alternating to black)
    * multiple blinking colors
* Sending the color in the format <span style="color: red;">lightwait-tp</span> text protocol format to UDP Port 3000 on localhost
* Usable both with python2 and python3 (tested with 2.7.15 and 3.6.8 on Ubuntu 18.04)

## Usage

Currently these lightwait-presenters are able to communication via UDP:

* lightwait-python-gtk

If a presenter is listening on localhost udp port 3000, just call the transmitter using the <span style="color: red;">lightwait-tm-cli API</span>:

```
./lightwait-udp.py white
./lightwait-udp.py -b white
./lightwait-udp.py red green
```

If your python is not available by `/usr/bin/env` or the `/usr/bin/env` command is not available, just call them like this:

```
path/to/your/python(2/3): lightwait-udp.py white
path/to/your/python(2/3): lightwait-udp.py -b white
path/to/your/python(2/3): lightwait-udp.py red green
```
## Tested on

| OS | Version | python | Result
|-|-|-|-
| Ubuntu | 18.04 | 2.7.15+ | ✔
| Ubuntu | 18.04 | 3.6.8 | ✔
| Ubuntu | 18.04 | 3.7.3 | ✔
