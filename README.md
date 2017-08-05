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
    - [Relays](#relays)
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
>>> from taliabeeio import TaliaBeeIO
>>> io = TaliaBeeIO()
>>>
>>> # read from the analog input 3
>>> print(io.ai3)
0
>>> # write to the analog output 4
>>> io.ao4 = 250
>>>
>>> # set the relay 13
>>> io.ro13 = True
>>>
>>> # reset the digital output 9
>>> io.do9 = False
>>>
>>> # read the temperature
>>> print(io.temperature)
37.125
>>> # reset all outputs
>>> io.reset()
```

TaliaBeeIO object
=================
```python
TaliaBeeIO(url='http://127.0.0.1', timeout=10, verify=False)
```

Create a new TaliaBeeIO instance. The instance communicates with the TaliaBee box at the given `url`. The default value is `http://127.0.0.1` and the instance communicates with the local box, if there is no given `url`.

`timeout` sets the socket timeout value. The default value is 10 seconds.

`verify` is the SSL certificate verification when HTTPS is used in `url`. Set `False` when the self-signed certificate is used and this is the situation in most cases.

```python
>>> from taliabeeio import TaliaBeeIO
>>> io_local = TaliaBeeIO()
>>> print(io_local.ai3)
1350
>>> io_remote = TaliaBeeIO(url='http://192.168.0.10')
>>> print(io_remote.ai3)
0
```

Digital inputs
--------------
Read-only digital inputs. `diN` where N is a number from `1` to `16`. Its value is either `0` or `1`.

```python
>>> print(io.di5)
0
```

Digital outputs
---------------
Writable digital outputs. `doN` where N is a number from `1` to `12`. Its value is either `0`/`False` or `1`/`True`.

```python
>>> print(io.do12)
0
>>> io.do12 = True
>>> print(io.do12)
1
```

Relays
------
Writable relay outputs. `roN` where N is a number from `13` to `16`. Its value is either `0`/`False` or `1`/`True`.

```python
>>> print(io.ro14)
0
>>> io.ro14 = True
>>> print(io.ro14)
1
```

Analog inputs
-------------
Read-only 12 bit analog inputs. `aiN` where N is a number from `1` to `4`. Its value is between 1 and 4095.

```python
>>> print(io.ai1)
0
```

Analog outputs
--------------
Writable 12 bit analog outputs. `aoN` where N is a number from `1` to `4`. Its value is between 1 and 4095.

```python
>>> print(io.ao4)
0
>>> io.ao4 = 2000
>>> print(io.ao4)
2000
```

Temperature
-----------
Read-only temperature value in Celsius.

```python
>>> print(io.temperature)
37.625
```

Status
------
The dictionary object which contains the values of all digital and analog I/O and the temperature.

```python
>>> print(io.status)
{'di': {'2': 0, '8': 0, '13': 0, '7': 0, '11': 0, '15': 0, '14': 0, '6': 0,
'10': 0, '16': 0, '1': 0, '4': 0, '9': 0, '3': 0, '12': 0, '5': 0},
'do': {'2': 0, '8': 0, '7': 0, '11': 0, '6': 0, '10': 0, '1': 0, '4': 0,
'9': 0, '3': 0, '12': 1, '5': 0}, 'temperature': 37.625, 'ro': {'15': 0,
'14': 1, '13': 0, '16': 0}, 'ai': {'2': 0, '1': 1, '4': 0, '3': 1},
'ao': {'2': 0, '1': 0, '4': 2000, '3': 0}}
```

di_read method
--------------
```python
di_read(pin)
```

Return the value of the digital input. `pin` is the digital input pin number and it's an integer between 1 and 16. The returning value is either `0` or `1`.

```python
>>> print(io.di_read(2))
0
```

do_read method
--------------
```python
do_read(pin)
```

Return the value of the digital output. `pin` is the digital output pin number and it's an integer between 1 and 12. The returning value is either `0` or `1`.

```python
>>> print(io.do_read(8))
0
```

do_set method
-------------
```python
do_set(pin)
```

Set the digital output. `pin` is the digital output pin number and it's an integer between 1 and 12.

```python
>>> print(io.do8)
0
>>> io.do_set(8)
>>> print(io.do8)
1
```

do_reset method
---------------
```python
do_reset(pin)
```

Reset the digital output. `pin` is the digital output pin number and it's an integer between 1 and 12.

```python
>>> print(io.do8)
1
>>> io.do_reset(8)
>>> print(io.do8)
0
```

do_write method
---------------
```python
do_write(pin, value)
```

Write to the digital output. `pin` is the digital output pin number and it's an integer between 1 and 12. `value` is either `0`/`False` or `1`/`True`.

```python
>>> print(io.do3)
0
>>> io.do_write(3, True)
>>> print(io.do3)
1
```

ro_read method
--------------
```python
ro_read(pin)
```

Return the value of the relay output. `pin` is the relay output pin number and it's an integer between 13 and 16. The returning value is either `0` or `1`.

```python
>>> print(io.ro_read(14))
0
```

ro_set method
-------------
```python
ro_set(pin)
```

Set the relay output. `pin` is the relay output pin number and it's an integer between 13 and 16.

```python
>>> print(io.ro14)
0
>>> io.ro_set(14)
>>> print(io.ro14)
1
```

ro_reset method
---------------
```python
ro_reset(pin)
```

Reset the relay output. `pin` is the relay output pin number and it's an integer between 13 and 16.

```python
>>> print(io.ro14)
1
>>> io.ro_reset(14)
>>> print(io.ro14)
0
```

ro_write method
---------------
```python
ro_write(pin, value)
```

Write to the relay output. `pin` is the relay output pin number and it's an integer between 13 and 16. `value` is either `0`/`False` or `1`/`True`.

```python
>>> print(io.ro14)
0
>>> io.ro_write(14, True)
>>> print(io.ro14)
1
```

ai_read method
--------------
```python
ai_read(pin)
```

Return the value of the analog input. `pin` is the analog input pin number and it's an integer between 1 and 4. The returning value is an integer between 1 and 4095.

```python
>>> print(io.ai_read(2))
8
```

ao_read method
--------------
```python
ao_read(pin)
```

Return the value of the analog output. `pin` is the analog output pin number and it's an integer between 1 and 4. The returning value is an integer between 1 and 4095.

```python
>>> print(io.ao_read(2))
0
```

ao_write method
---------------
```python
ao_write(pin, value)
```

Write to the analog output. `pin` is the analog output pin number and it's an integer between 1 and 4. `value` is an integer between 1 and 4095.

```python
>>> print(io.ao2)
0
>>> io.ao_write(2, 500)
>>> print(io.ao2)
500
```

reset method
------------
```python
reset()
```

Reset all digital and analog outputs.

```python
>>> io.do3 = True
>>> io.ao4 = 1350
>>> print(io.do3, io.ao4)
1 1350
>>> io.reset()
>>> print(io.do3, io.ao4)
0 0
```
