import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

note = input().strip()
keyword = input().strip()
a = ""
for n in note:
    if 48<= ord(n) <= 57:
        continue
    a += n
if keyword in a:
    print(1)
else:
    print(0)