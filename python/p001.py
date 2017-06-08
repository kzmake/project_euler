#/usr/bin/env python

def calc():
    result = sum(x for x in range(1000) if (x % 3 == 0 or x % 5 == 0))
    return result

if __name__ == "__main__":
    print(calc())
