s1 = 'abc'
s2 = 'abcd'
# print(s1<s2)
# print(s2<s1)
# print(s1 == s2)


def atoi(s):
    i = 0
    for x in s:
        i = i*10 + ord(x)-ord('0')
    return i

a = '123'
print(atoi(a))
print(type(atoi(a)))