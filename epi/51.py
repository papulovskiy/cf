def parity(num):
    p = 0
    for i in range(0, 64):
        p = p ^ (1 if num & (1 << i) else 0)
    return p

if __name__ == "__main__":
    print(parity(13))
