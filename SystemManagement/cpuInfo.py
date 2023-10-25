import os
import sys
import psutil
from psutil._common import bytes2human


def main():
    cpu_times_data = get_cpu_times()
    cpu_usage_data = get_cpu_usage()
    cpu_freq_data = get_cpu_freq()
    data = {
        "times": cpu_times_data,
        "usage": cpu_usage_data,
        "freq": cpu_freq_data
    }
    return data


def get_cpu_times(n=None):
    templ = "%-2s %-6s %12s %12s %12s %12s"
    cpu_times_data = None

    cpu_times_per = psutil.cpu_times(percpu=True)
    print("--------------------[      CPU TIMES       ]--------------------")
    print(templ % ("No", "Cpu", "User", "Nice", "System", "Idle"))
    if(n == None):
        cpu_times = psutil.cpu_times(percpu=False)
        cpu_times_data = cpu_times
        print(templ % ("-", "All", cpu_times.user,
              cpu_times.nice, cpu_times.system, cpu_times.idle))
        for idx in range(len(cpu_times_per)):
            print(templ % (idx, "CPU"+str(idx), cpu_times_per[idx].user,
                           cpu_times_per[idx].nice, cpu_times_per[idx].system, cpu_times_per[idx].idle))
    elif(n < len(cpu_times_per)):
        cpu_times_data = cpu_times_per[n]
        print(templ % (n, "CPU"+str(n), cpu_times_per[n].user,
                       cpu_times_per[n].nice, cpu_times_per[n].system, cpu_times_per[n].idle))
    else:
        print(f"[Error] invalid partition index, index={n}")
    return cpu_times_data


def get_cpu_usage(n=None):
    templ = "%-2s %-6s %6s"
    cpu_usage_data = None

    cpu_usage_per = psutil.cpu_percent(percpu=True)
    print("--------------------[      CPU USAGE       ]--------------------")
    print(templ % ("No", "Cpu", "Usage"))
    if(n == None):
        cpu_usage = psutil.cpu_percent(percpu=False)
        cpu_usage_data = cpu_usage
        print(templ % ("-", "All", cpu_usage))
        for idx in range(len(cpu_usage_per)):
            print(templ % (idx, "CPU"+str(idx),
                  cpu_usage_per[idx]))
    elif(n < len(cpu_usage_per)):
        cpu_usage_data = cpu_usage_per[n]
        print(templ % (n, "CPU"+str(n), cpu_usage_per[n]))
    else:
        print(f"[Error] invalid partition index, index={n}")
    return cpu_usage_data


def get_cpu_freq(n=None):
    templ = "%-2s %-6s %10s %10s %10s"
    cpu_freq_data = None

    cpu_freq_per = psutil.cpu_freq(percpu=True)
    print("--------------------[      CPU USAGE       ]--------------------")
    print(templ % ("No", "Cpu", "Current", "Min", "Max"))
    if(n == None):
        cpu_freq = psutil.cpu_freq(percpu=False)
        cpu_freq_data = cpu_freq
        print(templ % ("-", "All", cpu_freq.current, cpu_freq.min, cpu_freq.max))
        for idx in range(len(cpu_freq_per)):
            print(templ % (idx, "CPU"+str(idx),
                  cpu_freq_per[idx].current, cpu_freq_per[idx].min, cpu_freq_per[idx].max))
    elif(n < len(cpu_freq_per)):
        cpu_freq_data = cpu_freq_per[n]
        print(templ % (n, "CPU"+str(n),
              cpu_freq_per[n].current, cpu_freq_per[n].min, cpu_freq_per[n].max))
    else:
        print(f"[Error] invalid partition index, index={n}")
    return cpu_freq_data


if __name__ == "__main__":
    main()
