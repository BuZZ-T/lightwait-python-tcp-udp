# lightwait-python-tcp-udp

This is a [transmitter](https://github.com/BuZZ-T/lightwait#transmitter) for TCP- or UDP-based presenters in the [lightwait-stack](https://github.com/BuZZ-T/lightwait).

## Features

* Written in a few lines of python (~100)
* Supports multiple formats as input
    * known color names ("white", "black", "red", ...) See full list: [known colors](https://github.com/BuZZ-T/lightwait#known-colors)
    * case-insensitive 3-digit hex code without the leading # (e.g. "F00", meaning "#FF0000")
    * case-insensitive 6-digit hex code without the leading # (e.g. "FF0000")
* Supports
    * solid color
    * blinking color (alternating to black)
    * multiple blinking colors
* Sending the color in the format [lightwait-tp](https://github.com/BuZZ-T/lightwait#transmitter---presenter) communication protocol to TCP Port or UDP Port 3030 on localhost
* Usable both with python2 and python3 (see [Tested on](#tested))
* "Configurable" whether to use TCP or UDP via constant in the first lines of the code

## Usage

Currently these lightwait-presenters are able to communicate via UDP:

* [lightwait-python-gtk](https://github.com/BuZZ-T/lightwait-python-gtk)
* [lightwait-js-web-extension](https://github.com/BuZZ-T/lightwait-js-web-extension)

Currently these lightwait-presenters are able to communicate via TCP:

* [lightwait-gnome-extension](https://github.com/BuZZ-T/lightwait-gnome-extension)

If a presenter is listening on port 3030, just call the transmitter using the [lightwait-tp](https://github.com/BuZZ-T/lightwait#transmitter---presenter) communication protocol.

```
./lightwait-tcp-udp.py white
./lightwait-tcp-udp.py -b white
./lightwait-tcp-udp.py red green
```
You can set the protocol in two ways:

* Changing the `PROTOCOL` variable directly in the code. Available values are "TCP" or "UDP", both uppercase
* Changing the name of the python script (the easiest way is to create a symlink). If the name contains "tcp" but not "udp", a TCP connection is used and vice versa.
    E.g.: `ln -s lightwait-tcp-udp.py lightwait-udp.py` for UDP and `ln -s lightwait-tcp-udp.py lightwait-tcp.py` for TCP.


<a name="tested"></a>
## Tested on

| OS | Version | python | Result
|-|-|-|-
| Ubuntu | 18.04 | 2.7.15+ | ✔
| Ubuntu | 18.04 | 3.6.8 | ✔
| Ubuntu | 18.04 | 3.7.3 | ✔
| Ubuntu | 18.04 | pypy 5.10.0 (for 2.7.13) via aptitude | ✔
| Ubuntu | 18.04 | pypy 5.10.1 (for 3.5.3) via snap | ✔
