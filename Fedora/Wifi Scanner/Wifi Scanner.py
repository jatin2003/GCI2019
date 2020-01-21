# Python Script to check who is on your WiFI

import subprocess

results = subprocess.check_output(["netsh", "wlan", "show", "network"])
results = results.decode("ascii")
results = results.replace("\r","")
ls = results.split("\n")
ls = ls[4:]
ssids = []

n = 0

while n < len(ls):
    if n % 5 == 0:
        ssids.append(ls[n])
    n += 1
print(ssids)
