import os
import sys
import psutil
from psutil._common import bytes2human


def main():
    templ = "%-17s %8s %8s %8s %5s%% %9s  %s"
    print(templ % ("Device", "Total", "Used", "Free", "Use ", "Type",
                   "Mount"))
    for part in psutil.disk_partitions(all=False):
        if os.name == 'nt':
            if 'cdrom' in part.opts or part.fstype == '':
                # skip cd-rom drives with no disk in it; they may raise
                # ENOENT, pop-up a Windows GUI error for a non-ready
                # partition or just hang.
                continue
        usage = psutil.disk_usage(part.mountpoint)
        print(templ % (
            part.device,
            bytes2human(usage.total),
            bytes2human(usage.used),
            bytes2human(usage.free),
            int(usage.percent),
            part.fstype,
            part.mountpoint))


def help(lang="en"):
    infoEn = """device: the device path (e.g. "/dev/hda1"). On Windows this is the drive letter (e.g. "C:\\").
mountpoint: the mount point path (e.g. "/"). On Windows this is the drive letter (e.g. "C:\\").
fstype: the partition filesystem (e.g. "ext3" on UNIX or "NTFS" on Windows).
maxfile: the maximum length a file name can have.
maxpath: the maximum length a path name (directory name + base file name) can have.
opts: a comma-separated string indicating different mount options for the drive/partition. Platform-dependent."""
    infoKo = """device : 장치 경로(예: "/dev/hda1"). Windows에서는 드라이브 문자입니다(예: "C:\\").
mountpoint : 마운트 지점 경로(예: "/"). Windows에서는 드라이브 문자입니다(예: "C:\\").
fstype : 파티션 파일 시스템(예 "ext3": UNIX 또는 "NTFS" Windows).
maxfile : 파일 이름이 가질 수 있는 최대 길이입니다.
maxpath : 경로 이름(디렉터리 이름 + 기본 파일 이름)이 가질 수 있는 최대 길이입니다.
opts : 드라이브/파티션에 대한 다양한 마운트 옵션을 나타내는 쉼표로 구분된 문자열입니다. 플랫폼에 따라 다릅니다."""
    print("--------------------[         INFO         ]--------------------")
    if lang == "en":
        print(infoEn)
    elif lang == "ko":
        print(infoKo)
    return False


def get_partitions(n=None):
    templ = "%-2s %-17s %-32s %9s %8s %8s %s"
    partition_data = None

    partitions = psutil.disk_partitions()
    print("--------------------[      PARTITIONS      ]--------------------")
    print(templ % ("No", "Device", "Mountpoint",
          "Fstype", "Maxfile", "Maxpath", "Opts"))
    if n == None:
        partition_data = partitions
        for idx in range(len(partitions)):
            print(templ % (idx, partitions[idx].device, partitions[idx].mountpoint, partitions[idx].fstype,
                  partitions[idx].maxfile, partitions[idx].maxpath, partitions[idx].opts))
    elif n < len(partitions):
        partition_data = partitions[n]
        print(templ % (n, partitions[n].device, partitions[n].mountpoint, partitions[n].fstype,
                       partitions[n].maxfile, partitions[n].maxpath, partitions[n].opts))
    else:
        print(f"[Error] invalid partition index, index={n}")
    return partition_data


def get_usage(n=None):
    templ = "%-2s %-17s %8s %8s %8s %5s%%"
    tempa = []
    usage_data = None
    print("--------------------[        USAGE         ]--------------------")
    print(templ % ("No", "Device", "Total", "Used", "Free", "Use "))
    if n == None:
        n = 0
        tempa = psutil.disk_partitions(all=False)
    elif n < len(psutil.disk_partitions(all=False)):
        tempa = [psutil.disk_partitions(all=False)[n]]
    else:
        print(f"[Error] invalid partition index, index={n}")

    if tempa != []:
        for part in tempa:
            usage = psutil.disk_usage(part.mountpoint)
            print(templ % (
                n,
                part.device,
                bytes2human(usage.total),
                bytes2human(usage.used),
                bytes2human(usage.free),
                int(usage.percent),))
            n += 1
    return usage_data


if __name__ == '__main__':
    sys.exit(main())
