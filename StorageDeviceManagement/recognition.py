import os

diskInfo = os.statvfs('/')
used = diskInfo.f_bsize * (diskInfo.f_blocks - diskInfo.f_bavail)
free = diskInfo.f_bsize * diskInfo.f_bavail
total = diskInfo.f_bsize * diskInfo.f_blocks
print(used)
print(free)
print(total)

os.path.isdir() 