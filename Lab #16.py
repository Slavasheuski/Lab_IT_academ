import time
import os

l = [1]
a = 1

while True:
    a += 1
    print(*l)
    l[0] = a
    time.sleep(1)
    os.system('cls')
