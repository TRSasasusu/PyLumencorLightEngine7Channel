# lle7ch (PyLumencorLightEngine7Channel)
Controls [SOLA light engine](https://lumencor.com/products/sola-light-engine/). It covers [this document](https://lumencor.com/wp-content/uploads/sites/11/2016/02/Spectra-TTL-IF-Doc.pdf).

## Usage
```python
>>> from main import LLE
>>> lle = LLE()
>>> lle.enable_lights_disable_others({LLE.Light.RED, LLE.Light.BLUE}) # Enable Red and Blue LED, and disable other lights.
>>> lle.tune_intensity(LLE.Light.RED, 128) # Set intensity of Red LED as 128. (Min: 0, Max: 255)
>>> lle.enable_lights_disable_others({}) # Disable all lights.
>>> lle.read_temperature()
40.0
>>>
```

## License
GNU General Public License v3.0
