#!/usr/bin/env python3

from network import *
import shutil
import psutil


def check_disk_usage(disk):
    du = shutil.disk_usage(disk)
    free = du.free / du.total * 100
    return free > 20


def check_cpu_usage():
    usage = psutil.cpu_percent(1)
    return usage < 75


if not check_disk_usage("/") or not check_cpu_usage():
    print("ERROR!")
elif check_localhost() and check_connectivity():
    print("Everything is OK!")
else:
    print("Network checks failed")
