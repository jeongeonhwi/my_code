import sys
input = sys.stdin.readline

N = int(input())
arr = input().strip()
# alpabet = 'abcdefghijklmnopqrstuvwxyz'
alpabet = {'a':0,'b':1,'c':2,'d':3,'e':4,'f':5,'g':6,'h':7,'i':8,'j':9,'k':10,'l':11,'m':12,'n':13,'o':14,'p':15,'q':16,'r':17,'s':18,'t':19,'u':20,'v':21,'w':22,'x':23,'y':24,'z':25}
ans = 0
for i in range(N):
    ans += (alpabet[arr[i]]+1)*(31**i)
print(ans%1234567891)

# L = int(input())
# M = 1234567891
# r = 31
# user_input = input()
#
# answer = 0
#
# for i in range(len(user_input)):
#     num = ord(user_input[i]) - 96
#     answer += num * (r ** i)
#
# print(answer % M)