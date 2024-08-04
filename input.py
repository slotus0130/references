## 첫째 줄에 전체 입력 수, 둘째 줄에 숫자가 띄어쓰기로 구분되어 주어질 때

### VS Code에서 테스트하기 위한 코드
N = 5
input_numbers = "4 3 1 2 5" # 입력은 띄어쓰기로 구분된 문자열

numbers = [int(n) for n in input_numbers.split()]
print(numbers) # 결과는 [4, 3, 1, 2, 5]

### 대회에서 업로드하기 위한 코드
N = int(input())
input_numbers = input()

numbers = [int(n) for n in input_numbers.split()]
print(numbers)
