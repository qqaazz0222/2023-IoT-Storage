import os
import sys
import psutil
from psutil._common import bytes2human


def main():
    virtual_data = get_memory_virtual()
    swap_data = get_memory_swap()
    memory_data = {
        "virtual": virtual_data,
        "swap": swap_data
    }
    return memory_data


def get_memory_virtual():
    memory_data = psutil.virtual_memory()
    print("--------------------[    Virtual Memory    ]--------------------")
    pprint_ntuple(memory_data)
    return memory_data


def get_memory_swap():
    memory_data = psutil.swap_memory()
    print("--------------------[     SWAP Memory      ]--------------------")
    pprint_ntuple(memory_data)
    return memory_data


def pprint_ntuple(nt):
    for name in nt._fields:
        value = getattr(nt, name)
        if name != 'percent':
            value = bytes2human(value)
        print('%-10s : %7s' % (name.capitalize(), value))


if __name__ == "__main__":
    main()
