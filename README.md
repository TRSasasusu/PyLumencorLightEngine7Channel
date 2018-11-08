[![PyPI version](https://badge.fury.io/py/lle7ch.svg)](https://badge.fury.io/py/lle7ch)

# lle7ch (PyLumencorLightEngine7Channel)
Controls [SOLA light engine](https://lumencor.com/products/sola-light-engine/). It covers [this document](https://lumencor.com/wp-content/uploads/sites/11/2016/02/Spectra-TTL-IF-Doc.pdf).

## Install
```
pip install lle7ch
```

## Usage
### From Python Script
```python
>>> from lle7ch import LLE
>>> lle = LLE()
>>> lle.enable_lights_disable_others({LLE.Light.RED, LLE.Light.BLUE}) # Enable Red and Blue LED, and disable other lights.
>>> lle.tune_intensity(LLE.Light.RED, 128) # Set intensity of Red LED as 128. (Min: 0, Max: 255)
>>> lle.enable_lights_disable_others({}) # Disable all lights.
>>> lle.read_temperature()
40.0
>>>
```
### CLI Tool
You can make a plan to control LLE automatically.  
`r: LLE.Light.RED, g: LLE.Light.GREEN, c: LLE.Light.CYAN, u: LLE.Light.UV, b: LLE.Light.BLUE, t: LLE.Light.TEAL`

```bash
$ cat plan.txt
set g,128
on g
wait 5

set b,255
on b,g
wait 5
$ lleplan plan.txt
```

## License
GNU General Public License v3.0
