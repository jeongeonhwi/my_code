a = '가나다라마바사아자차카타 #윤여정 #사랑해 #코미디'
b = ''
check = False
for i in a:
    if i == '#':
        check = True
    if check:
        b+=i
c = b.split(' ')
print(c)