# A python script that cubes all odd numbers from 0 to 19 or the original number if it is even.

def cb(val):
    return val ** 3

for x in range(20):
    if (x % 2) == 0:
        print x
    else:
        print cb(x)
