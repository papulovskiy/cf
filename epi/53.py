def rev(num):
    result = 0
    limit = 31
    comp = 1 << limit
    while not num & comp:
        comp = comp >> 1
        limit -= 1
    limit += 1
    for x in range(0, limit):
        result = result | ((1 if num & (1 << x) else 0) << (limit - 1 - x))
    return result

if __name__ == "__main__":
    print(rev(65536))
    print(rev(5))
