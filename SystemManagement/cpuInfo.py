import psutil

cpu = psutil.cpu_times_percent()
usage = psutil.cpu_percent(interval=None, percpu=False)
usage_per_cpu = psutil.cpu_percent(interval=None, percpu=True)
idel = cpu.idle
logi_core = psutil.cpu_count()
pysi_core = psutil.cpu_count(logical=False)
times = psutil.cpu_times(percpu=False)

if __name__ == "__main__":
    print(
        f"CPU 사용율 : {usage}%, 유휴 CPU : {idel}%, 논리적 코어 수 : {logi_core}, 물리적 코어 수 : {pysi_core}, 동작 시간 : {times.user + times.system}초")
