## 3x3 행렬

```python
import sys

li = [[1, 5, 3], [2, 4, 7], [5, 3, 5]]
chk = [False] * 3
m = sys.maxsize

def backtracking(row, score):
    global m
    
    if row == 3:  # 재귀함수를 마치는 조건
        m = min(m, score)
        return

    for i in range(3):
        if promising(chk[i]):  # 백트래킹에서의 한정조건
            chk[i] = True
            backtracking(row + 1, score + li[row][i])
            chk[i] = False

def promising(check: bool):
    if not check:
        return True
    
    return False

backtracking(0, 0)
print(m)
```

## n-Queens 문제

```python
n = int(input())

ans = 0
row = [0] * n

def is_promising(x):
    for i in range(x):
        # x행에 위치한 퀸과 i행에 위치한 퀸의 열이 같거나, 행 차이와 열 차이가 같은 경우 (대각선)
        if row[x] == row[i] or abs(row[x] - row[i]) == abs(x - i):
            return False
    
    return True

def n_queens(x):
    global ans
    if x == n:
        ans += 1
        return

    else:
        for i in range(n):
            # [x, i]에 퀸을 놓겠다.
            row[x] = i
            if is_promising(x):
                n_queens(x+1)

n_queens(0)
print(ans)
```
