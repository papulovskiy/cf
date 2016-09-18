def swap(num, i, j):
    bi = 1 if num & (1 << i) else 0
    bj = 1 if num & (1 << j) else 0
    if bi == 1:
        num = num | (1 << j)
    elif bj == 1:
        num = num ^ (1 << j)

    if bj == 1:
        num = num | (1 << i)
    elif bi == 1:
        num = num ^ (1 << i)

    return num

if __name__ == "__main__":
    print(swap(65536, 16, 5))
    print(swap(65536, 15, 5))
