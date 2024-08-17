## Case 1: 첫째 줄에 전체 입력 수, 둘째 줄에 숫자가 띄어쓰기로 구분되어 주어짐

```
5
1 2 3 4 5
```

#### VS Code 테스트
```python
N = 5
input_numbers = "4 3 1 2 5" # 입력은 띄어쓰기로 구분된 문자열

numbers = [int(n) for n in input_numbers.split()]
print(numbers)

# 결과는 [4, 3, 1, 2, 5]
```

#### 업로드
```python
N = int(input())
input_numbers = input()

numbers = [int(n) for n in input_numbers.split()]
print(numbers)

# 결과는 [4, 3, 1, 2, 5]
```

## Case 2: 첫째 줄에서 첫 번째 값은 초기 값, 두 번째 값은 전체 라인 수

초기 값은 10이며 아래에 3개의 라인이 존재함
```
10 3
2 20
1 10
3 40
```

#### VS Code 테스트
```python
init_value = 10
number_of_lines = 3

# 입력 데이터가 각 줄에 띄어쓰기로 구분되어 주어짐.
input_data = """2 20
1 10
3 40"""

# input_data를 list로 변환
lines = [list(map(int, line.split())) for line in input_data.split('\n')]

for line in lines:
    print(f"first value: {line[0]}, second value: {line[1]}")

# 결과는,
# first value: 2, second value: 20
# first value: 1, second value: 10
# first value: 3, second value: 40
```


#### 업로드
```python
init_value, number_of_lines = map(int, input().split())
lines = [list(map(int, input().split())) for _ in range(number_of_lines)]

for line in lines:
    print(f"first value: {line[0]}, second value: {line[1]}")

# 결과는,
# first value: 2, second value: 20
# first value: 1, second value: 10
# first value: 3, second value: 40
```

## Case 3: 첫째 줄의 값은 다음 라인들에 올 재료의 가지 수, 두 번째 줄은 창고에 있는 각 재료의 수, 세 번째 줄은 요리에 필요한 각 재료의 수

```
3
6 3 5
1 1 2
```

#### VS Code 테스트

```python
input_data = """3
6 3 5
1 1 2"""

# 입력을 줄 단위로 나누기
lines = input_data.split('\n')

# 재료의 가짓수
n = int(lines[0])

# 창고에 있는 재료의 수량
stock = list(map(int, lines[1].split()))

# 스테이크를 만드는데 필요한 재료의 수량
recipe = list(map(int, lines[2].split()))

# 결과는,
# n: 3, stock: [6, 3, 5], recipe: [1, 1, 2]
```

#### 업로드
```python
n = int(input())
stock = list(map(int, input().split()))
recipe = list(map(int, input().split()))

print(f"n: {n}, stock: {stock}, recipe: {recipe}")

# 결과는,
# n: 3, stock: [6, 3, 5], recipe: [1, 1, 2]
```

## Case 4: 첫째 줄의 값은 다음 라인들에 올 모든 직업의 수(문자열), 직업 이름들 아래의 값은 다음 라인들에 올 내 직업의 수(문자열)
```
2
Hero
Paladin
1
Hero
```

#### VS Code 테스트

```python
N = 2

input_data = """Hero
Paladin"""

# 입력을 줄 단위로 나누기
all_jobs = input_data.split('\n')
print(all_jobs)

# 결과는,
# ['Hero', 'Paladin']

K = 1

input_data = """Paladin"""

# 입력을 줄 단위로 나누기
my_jobs = input_data.split('\n')
print(my_jobs)

# 결과는,
# ['Hero']
```

#### 업로드
```python
N = int(input())

# 입력을 줄 단위로 나누기
all_jobs = [input() for _ in range(N)]
print(all_jobs)

# 결과는,
# ['Hero', 'Paladin']

K = int(input())

# 입력을 줄 단위로 나누기
my_jobs = [input() for _ in range(K)]
print(my_jobs)

# 결과는,
# ['Hero']
```

## Case 5: 첫째 줄의 값은 다음 라인들에 올 모든 문자열의 수(문자열), 다음 라인들은 띄어쓰기로 구분되는 문자열

```
2
WC2B 5RL
SW20 8RR
```

#### VS Code 테스트

```python
N = 2

input_data = """WC2B 5RL
SW20 8RR"""

for _line in input_data.split('\n'):
    line = _line.split()
    print(f"line[0]: {line[0]}, line[1]: {line[1]}")
```

#### 업로드

```python
N = int(input())

for _ in range(N):
    line = list(input().split())
    print(f"line[0]: {line[0]}, line[1]: {line[1]}")
```

## Case 6: 첫째 줄에 전체 입력 수, 둘째 줄에 숫자가 띄어쓰기로 구분되어 주어짐

#### VS Code 테스트

```python
N = 5
input_numbers = "4 3 1 2 5"

for n in map(int, input_numbers.split()):
    print(n)
```

#### 업로드

```python
N = int(input())

for i in range(N):
    for c in input().split():
        print(c)
```
