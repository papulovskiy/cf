def strtoint(s):
    ch = {
        "0": 0,
        "1": 1,
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9
    }
    result = 0
    negative = False
    l = len(s)
    for i in range(0, l):
        if s[i] == "-" and i == 0:
            negative = True
            continue
        if s[i] in ch:
            result += ch[s[i]] * 10 ** (l - i - 1)
        else:
            return None
    if negative:
        result *= -1
    return result

def inttostr(i):
    ch = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    result = ""
    if i < 0:
        i *= -1
        result = "-"

    r = i // 10
    current = i - r * 10
    if r == 0 and current == 0:
        return ""
    else:
        return result + inttostr(r) + ch[current]
   
    


if __name__ == "__main__":
    print(strtoint("-0123801"))
    print(inttostr(329012))
