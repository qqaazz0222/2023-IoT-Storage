import os
import sys
import psutil
from psutil._common import bytes2human


def main(p=True):
    virtual_data = get_memory_virtual(p)
    swap_data = get_memory_swap(p)
    memory_data = {
        "virtual": virtual_data,
        "swap": swap_data
    }
    return memory_data


def get_memory_virtual(p=True):
    memory_data = psutil.virtual_memory()
    data = {}
    header = ["total", "available", "percent",
              "used", "free", "active", "inactive", "wired"]
    for idx in range(len(header)):
        data[header[idx]] = memory_data[idx]
    if p == True:
        print(
            "--------------------[    Virtual Memory    ]--------------------")
        pprint_ntuple(memory_data)
    return data


def get_memory_swap(p=True):
    memory_data = psutil.swap_memory()
    data = {}
    header = ["total", "used", "free", "percent", "sin", "sout"]
    for idx in range(len(header)):
        data[header[idx]] = memory_data[idx]
    if p == True:
        print(
            "--------------------[     SWAP Memory      ]--------------------")
        pprint_ntuple(memory_data)
    return data


def pprint_ntuple(nt):
    for name in nt._fields:
        value = getattr(nt, name)
        if name != 'percent':
            value = bytes2human(value)
        print('%-10s : %7s' % (name.capitalize(), value))


if __name__ == "__main__":
    main()
