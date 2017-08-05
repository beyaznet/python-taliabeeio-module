About
=====
TaliaBeeIO is a [Python](https://www.python.org/) interface to TaliaBee API. TaliaBeeIO can be used to monitor and to control the IO of TaliaBee box.

Table of contents
=================

- [About](#about)
- [Requirements](#requirements)
- [Installation](#installation)
- [Example](#example)

Requirements
============
- Python 3.x
- Python Requests module

Installation
============
```bash
pip3 install taliabeeio
```

Example
=======
```python
from taliabeeio import TaliaBeeIO
io = TaliaBeeIO()

# read from the analog input 3
print(io.ai3)

# write to the analog output 4
io.ao4 = 250

# set the relay 13
io.ro13 = True

# reset the digital output 9
io.do9 = False

# read the temperature
print(io.temperature)

# reset all outputs
io.reset()
```
