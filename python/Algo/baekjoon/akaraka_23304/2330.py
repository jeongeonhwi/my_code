import sys
sys.setrecursionlimit(100000)


def is_pelindrom(s):
    return True if s == s[::-1] else False


def solve(ss):
    global akaraka_pelindrom
    if len(ss) == 1:
        return ss

    half = int(len(ss)/2)
    if len(ss) % 2 == 0:
        b_half = ss[:half]
        a_half = ss[half:]
    else:
        b_half = ss[:half]
        a_half = ss[half+1:]
    if b_half != a_half:
        akaraka_pelindrom = False
    elif not is_pelindrom(ss):
        akaraka_pelindrom = False
    elif not is_pelindrom(solve(b_half)):
        akaraka_pelindrom = False
    return ss


s = input()
akaraka_pelindrom = True
solve(s)
print("AKARAKA" if akaraka_pelindrom else "IPSELENTI")