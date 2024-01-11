import matplotlib.pyplot as plt

# 예제1: x,y 가 같을 때
plt.plot([1,2,3,4])
# plt.show()

# 참고: 이때까지 그렸던 plot 지우기
plt.clf()

# 예제2: x, y가 다를때
x = [1,2,3,4]
y = [2,4,8,16]

# plt.plot(x,y)
# plt.show()

# 예제3: 제목 + 각 축의 설명
plt.plot(x,y)
# 제목
# 한글을 쓰면 깨진다. 추가적인 설정이 필요함. 구글링 요망
plt.title("Test Graph")

# x, y 축
plt.ylabel('y label')
plt.xlabel('x label')

# plt.show()

# 파일로 저장하기
# 주의사항: show()를 하지 말고 저장해야 한다.
plt.savefig('filename.png')