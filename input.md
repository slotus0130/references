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

#### 대회 업로드
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
lines = [tuple(map(int, line.split())) for line in input_data.split('\n')]

for line in lines:
    print(f"first value: {line[0]}, second value: {line[1]}")

# 결과는,
# first value: 2, second value: 20
# first value: 1, second value: 10
# first value: 3, second value: 40
```


#### 대회 업로드
```python
init_value, number_of_lines = map(int, input().split())

lines = [tuple(map(int, input().split())) for _ in range(number_of_lines)]

for line in lines:
    print(f"first value: {line[0]}, second value: {line[1]}")

# 결과는,
# first value: 2, second value: 20
# first value: 1, second value: 10
# first value: 3, second value: 40
```
