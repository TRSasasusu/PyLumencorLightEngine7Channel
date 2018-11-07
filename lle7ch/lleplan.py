# coding: utf-8

import sys
from time import sleep
from lle7ch import LLE


def Char2Light(c: str) -> LLE.Light:
    if c == 'r':
        return LLE.Light.RED
    if c == 'g':
        return LLE.Light.GREEN
    if c == 'c':
        return LLE.Light.CYAN
    if c == 'u':
        return LLE.Light.UV
    if c == 'b':
        return LLE.Light.BLUE
    if c == 't':
        return LLE.Light.TEAL


def main():
    with open(sys.argv[1], 'r') as f:
        plans = filter(lambda x: x != '', f.read().split('\n'))

    lle = LLE()
    for plan in plans:
        func, args = plan.split(' ')
        print(plan)
        if func == 'on':
            lle.enable_lights_disable_others({Char2Light(c) for c in args.split(',')})
        elif func == 'set':
            c, intensity = args.split(',')
            lle.tune_intensity(Char2Light(c), int(intensity))
        elif func == 'wait':
            sleep(float(args))
        else:
            print('Unknown function: {}'.format(plan))

if __name__ == '__main__':
    main()
