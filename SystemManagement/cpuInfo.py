import psutil

cpu_percent = psutil.cpu_percent()
cpu_times_percent = psutil.cpu_times_percent()
cpu_idel = psutil.cpu_idle()

print(cpu_percent)
print(cpu_times_percent)
print(cpu_idel)
