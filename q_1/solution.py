import sys
import time

#recusrive approach
def fact(x):
    if x == 0:
        return 1
    return x*fact(x-1)

def fact_loop(x):
    
    num = 1
    for i in range(2,x):
        num *= i
    return num


num = int(sys.argv[1])
t0 = time.time()
print "factorial of %d - %d needed %.3f s" % (num, fact(num), time.time() - t0)

print "loop factorial of %d -%d needed %.3f s" % (num,fact_loop(num),time.time() - t0)


