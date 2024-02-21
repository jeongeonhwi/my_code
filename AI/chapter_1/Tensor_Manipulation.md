# 텐서 조작하기(Tensor Manipulation)
https://wikidocs.net/52460
## 넘파이로 텐서 만들기(벡터와 행렬 만들기)
### 1D with Numpy
```python 
import numpy as np
t = np.array([0., 1., 2., 3., 4., 5., 6.])
# 파이썬으로 설명하면 List를 생성해서 np.array로 1차원 array로 변환함.
print(t)
# [0. 1. 2. 3. 4. 5. 6.]

print('Rank of t: ', t.ndim)
print('Shape of t: ', t.shape)
# Rank of t:  1
# Shape of t:  (7,)
```
* .ndim은 몇 차원인지를 출력합니다. 1차원은 벡터, 2차원은 행렬, 3차원은 3차원 텐서였습니다. 현재는 벡터이므로 1차원이 출력됩니다. .shape는 크기를 출력합니다. (7, )는 (1, 7)을 의미합니다. 다시 말해 (1 × 7)의 크기를 가지는 벡터입니다.
### Numpy 기초 이해하기
```python
print('t[2:5] t[4:-1]  = ', t[2:5], t[4:-1])
```
### 2D with Numpy