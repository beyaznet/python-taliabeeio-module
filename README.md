About
=====
TaliaBeeIO is a [Python](https://www.python.org/) interface to TaliaBee API. TaliaBeeIO can be used to monitor and to control the I/O pins of the TaliaBee box.

Table of contents
=================

- [About](#about)
- [Requirements](#requirements)
- [Installation](#installation)
- [Example](#example)
- [TaliaBeeIO object](#taliabeeio-object)
    - [Digital inputs](#digital-inputs)
    - [Digital outputs](#digital-outputs)
    - [Relay](#relay)
    - [Analog inputs](#analog-inputs)
    - [Analog outputs](#analog-outputs)
    - [Temperature](#temperature)
    - [Status](#status)
    - [di_read method](#di_read-method)
    - [do_read method](#do_read-method)
    - [do_set method](#do_set-method)
    - [do_reset method](#do_reset-method)
    - [do_write method](#do_write-method)
    - [ro_read method](#ro_read-method)
    - [ro_set method](#ro_set-method)
    - [ro_reset method](#ro_reset-method)
    - [ro_write method](#ro_write-method)
    - [ai_read method](#ai_read-method)
    - [ao_read method](#ao_read-method)
    - [ao_write method](#ao_write-method)
    - [reset method](#reset-method)

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

TaliaBeeIO object
=================
TaliaBeeIO(url='http://127.0.0.1', timeout=10, verify=False)

Create a new TaliaBeeIO instance. The instance communicates with the TaliaBee box at the given `url`. The default value is `http://127.0.0.1` and the instance communicates with the local box, if there is no given `url`.

`timeout` sets the socket timeout value. The default value is 10 seconds.

`verify` is the SSL certificate verification when HTTPS is used in `url`. Set `False` when the self-signed certificate is used and this is the situation in most cases.

```python
io = TaliaBeeIO(url='http://192.168.0.10')
```

Digital inputs
--------------
Read-only digital inputs. `diN` where N is a number from `1` to `16`. Its value is either `0` or `1`.

```python
print(io.di5)
```

Digital outputs
---------------
Writable digital outputs. `doN` where N is a number from `1` to `12`. Its value is either `0`/`False` or `1`/`True`.

```python
io.do12 = True
print(io.do12)
```

Relay
-----
Writable relay outputs. `roN` where N is a number from `13` to `16`. Its value is either `0`/`False` or `1`/`True`.

```python
io.ro14 = True
print(io.ro14)
```

Analog inputs
-------------
Read-only 12 bit analog inputs. `aiN` where N is a number from `1` to `4`. Its value is between 1 and 4095.

```python
print(io.ai1)
```

Analog outputs
--------------
Writable 12 bit analog outputs. `aoN` where N is a number from `1` to `4`. Its value is between 1 and 4095.

```python
io.ao4 = 2000
print(io.ao4)
```

Temperature
-----------

Status
------

di_read method
--------------

do_read method
--------------

do_set method
-------------

do_reset method
---------------

do_write method
---------------

ro_read method
--------------

ro_set method
-------------

ro_reset method
---------------

ro_write method
---------------

ai_read method
--------------

ao_read method
--------------

ao_write method
---------------

reset method
------------
