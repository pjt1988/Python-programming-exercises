import sys
import time


def array_loop(x):
    numbers = []
    for i in range(0,x+1):
        numbers.append(i*i)
    return numbers


def dict_loop(x):
    numbers = {}
    for i in range(1,x+1):
        numbers[i] = i*i
    return numbers


num = int(sys.argv[1])
t0 = time.time()
print dict_loop(num)
print "Dictionary loop needed %.2f s" % (time.time() - t0)
print array_loop(num)
print "Array loop needed %.2f s" % (time.time() - t0)


