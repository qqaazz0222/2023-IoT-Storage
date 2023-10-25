import os
import sys
import psutil
from psutil._common import bytes2human
import diskInfo
import time
from datetime import datetime
import logging

global diskList
global __log__
__log__ = "../Logs/detectdisk.txt"


def init():
    global diskList
    global __log__
    f = open(__log__, "a+")
    f.write(str(datetime.now()) + " Detect Start\n")
    diskList = diskInfo.get_partitions()
    f.close()


def detect_disk():
    global diskList
    global __log__
    interval = 1
    while True:
        print("Time :", datetime.now(), " / Current Disk Num : ", len(diskList))
        tempList = diskInfo.get_partitions(None, False)
        if len(tempList) != len(diskList):
            f = open(__log__, "a+")
            if len(tempList) > len(diskList):
                f.write(str(datetime.now()) + " New Storage Detect\n")
                for disk in tempList:
                    if disk not in diskList:
                        print("New Storage Detect!")
                        pprint_disk_info(disk)
            else:
                f.write(str(datetime.now()) + " A Storage Separated\n")
                for disk in diskList:
                    if disk not in tempList:
                        print("A Storage Separated!")
                        pprint_disk_info(disk)
            diskList = tempList
            f.close()
        time.sleep(interval)


def pprint_disk_info(disk):
    templ = "%-17s %-32s %9s %8s %8s %s"
    print(templ % ("Device", "Mountpoint",
                   "Fstype", "Maxfile", "Maxpath", "Opts"))
    print(templ % (disk.device, disk.mountpoint, disk.fstype,
                   disk.maxfile, disk.maxpath, disk.opts))


init()
detect_disk()
