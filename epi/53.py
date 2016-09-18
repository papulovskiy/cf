def rev(num):
    result = 0
    limit = 32
    for x in range(0, limit):
        result = result | ((1 if num & (1 << x) else 0) << (limit - 1 - x))
    return result

if __name__ == "__main__":
    print(rev(65536))
    print(rev(5))
