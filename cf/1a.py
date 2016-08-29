import math
import sys

for line in sys.stdin:
    line.strip()
    (n, m, a) = line.split(" ")
    n = int(n)
    m = int(m)
    a = int(a)
    print(math.ceil(n/a) * math.ceil(m/a))
