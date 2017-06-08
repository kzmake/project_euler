#/usr/bin/env python

def calc():
    result = 0
    x = 1
    y = 2

    while x <= 4000000:
        if x % 2 == 0:
            result += x
        x, y = y, x + y

    return result

if __name__ == "__main__":
    print(calc())
