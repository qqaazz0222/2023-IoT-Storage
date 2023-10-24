import sys
import time


try:
    import curses
except ImportError:
    sys.exit('platform not supported')

import psutil
from psutil._common import bytes2human


win = curses.initscr()
lineno = 0


def printl(line, highlight=False):
    global lineno
    try:
        if highlight:
            line += " " * (win.getmaxyx()[1] - len(line))
            win.addstr(lineno, 0, line, curses.A_REVERSE)
        else:
            win.addstr(lineno, 0, line, 0)
    except curses.error:
        lineno = 0
        win.refresh()
        raise
    else:
        lineno += 1


def poll(interval):
    # first get a list of all processes and disk io counters
    procs = list(psutil.process_iter())
    for p in procs[:]:
        try:
            p._before = p.io_counters()
        except psutil.Error:
            procs.remove(p)
            continue
    disks_before = psutil.disk_io_counters()

    # sleep some time
    time.sleep(interval)

    # then retrieve the same info again
    for p in procs[:]:
        with p.oneshot():
            try:
                p._after = p.io_counters()
                p._cmdline = ' '.join(p.cmdline())
                if not p._cmdline:
                    p._cmdline = p.name()
                p._username = p.username()
            except (psutil.NoSuchProcess, psutil.ZombieProcess):
                procs.remove(p)
    disks_after = psutil.disk_io_counters()

    # finally calculate results by comparing data before and
    # after the interval
    for p in procs:
        p._read_per_sec = p._after.read_bytes - p._before.read_bytes
        p._write_per_sec = p._after.write_bytes - p._before.write_bytes
        p._total = p._read_per_sec + p._write_per_sec

    disks_read_per_sec = disks_after.read_bytes - disks_before.read_bytes
    disks_write_per_sec = disks_after.write_bytes - disks_before.write_bytes

    # sort processes by total disk IO so that the more intensive
    # ones get listed first
    processes = sorted(procs, key=lambda p: p._total, reverse=True)

    return (processes, disks_read_per_sec, disks_write_per_sec)


def refresh_window(procs, disks_read, disks_write):
    """Print results on screen by using curses."""
    curses.endwin()
    templ = "%-5s %-7s %11s %11s  %s"
    win.erase()

    disks_tot = "Total DISK READ: %s | Total DISK WRITE: %s" \
                % (bytes2human(disks_read), bytes2human(disks_write))
    printl(disks_tot)

    header = templ % ("PID", "USER", "DISK READ", "DISK WRITE", "COMMAND")
    printl(header, highlight=True)

    for p in procs:
        line = templ % (
            p.pid,
            p._username[:7],
            bytes2human(p._read_per_sec),
            bytes2human(p._write_per_sec),
            p._cmdline)
        try:
            printl(line)
        except curses.error:
            break
    win.refresh()


def setup():
    curses.start_color()
    curses.use_default_colors()
    for i in range(curses.COLORS):
        curses.init_pair(i + 1, i, -1)
    curses.endwin()
    win.nodelay(1)


def tear_down():
    win.keypad(0)
    curses.nocbreak()
    curses.echo()
    curses.endwin()


def main():
    global lineno
    setup()
    try:
        interval = 0
        while True:
            if win.getch() == ord('q'):
                break
            args = poll(interval)
            refresh_window(*args)
            lineno = 0
            interval = 0.5
            time.sleep(interval)
    except (KeyboardInterrupt, SystemExit):
        pass
    finally:
        tear_down()


if __name__ == '__main__':
    main()
