# coding: utf-8

from functools import reduce
from enum import IntEnum, auto
from typing import Set
import serial


class LLE:
    class Light(IntEnum):
        RED = 0
        GREEN = auto()
        CYAN = auto()
        UV = auto()
        BLUE = 5
        TEAL = auto()

    def __init__(self, port='COM2'):
        self.serial = serial.Serial(port)

        # initialize commands
        self._send('5702FF50')
        self._send('5703AB50')

    def enable_lights_disable_others(self, lights: Set[Light], use_green_filter=True):
        core_code = reduce(lambda x, y: x - 2 ** y, lights, 2 ** 7 - 1)
        if not use_green_filter:
            # Use yellow filter not green filter.
            core_code -= 2 ** 4

        self._send('4F{:02X}50'.format(core_code))

    def tune_intensity(self, light: Light, intensity: float):
        if intensity < 0:
            intensity = 0
        if intensity > 255:
            intensity = 255

        if light in {LLE.Light.BLUE, LLE.Light.TEAL}:
            light_code = 1 if light == LLE.Light.BLUE else 2
            iic_addr = '1A'
        else:
            light_code = 2 ** (3 - light)
            iic_addr = '18'

        self._send('53{}030{:01X}F{:02X}050'.format(iic_addr, light_code, 255 - intensity))

    def read_temperature(self) -> float:
        self._send('53910250')
        hex_code = self.serial.read(2).hex()
        bin_code = '00' + bin(int(hex_code, 16))[2:].zfill(8)[:9]
        int_code = int(bin_code, 2)
        return int_code * 0.125

    def _send(self, code: str):
        self.serial.write(bytes.fromhex(code))
