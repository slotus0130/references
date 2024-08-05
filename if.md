## 비밀번호 유효한지 확인

### if문과 정규식을 사용한 버전

```python
import re
import sys

password = "{NYPC2019}"

if not (15 >= len(password) >= 8):
    print("invalid")
    sys.exit()

has_upper = False
for c in password:
    if c.isupper() == True:
        has_upper = True
if has_upper == False:
    print("invalid")
    sys.exit()

has_lower = False
for c in password:
    if c.islower() == True:
        has_lower = True
if has_lower == False:
    print("invalid")
    sys.exit()

has_numbers = False
for c in password:
    if c.isdigit() == True:
        has_numbers = True
if has_numbers == False:
    print("invalid")
    sys.exit()

if not re.search(r'[!@#$%^&*()\-=_+|;:\'"/?,.<>~\[\]{}]', password):
    print("invalid")
    sys.exit()

print("valid")
```

### 정규식만을 사용한 버전

```python
import re

password = "{NYPCc2019}"

def validate_password(password):
    # 비밀번호 길이 확인 (8자 이상 15자 이하)
    if len(password) < 8 or len(password) > 15:
        return False
    
    # 대문자, 소문자, 숫자, 특수문자 확인
    if not re.search(r'[A-Z]', password):
        return False
    if not re.search(r'[a-z]', password):
        return False
    if not re.search(r'\d', password):
        return False
    if not re.search(r'[!@#$%^&*()\-=_+|;:\'"/?,.<>~\[\]{}]', password):
        return False
    
    return True

result = validate_password(password)
if result == True:
    print("valid")
else:
    print("invalid")
```

### 이메일이 유효한지 확인
```python
import re

def is_valid_email(email):
    # 이메일이 '@' 기호로 나뉘어야 하고, 그 수는 정확히 1이어야 한다.
    if email.count('@') != 1:
        return "No"
    
    # 로컬 파트와 도메인 파트로 분리
    local_part, domain_part = email.split('@')
    
    # 로컬 파트와 도메인 파트의 길이 체크 (1자 이상 100자 이하)
    if not (1 <= len(local_part) <= 100) or not (1 <= len(domain_part) <= 100):
        return "No"
    
    # 유효한 문자 체크 (알파벳 대소문자, 숫자, '-', '.')
    valid_pattern = re.compile(r'^[A-Za-z0-9\-.]+$')
    if not valid_pattern.match(local_part) or not valid_pattern.match(domain_part):
        return "No"
    
    return "Yes"

# 입력받기
input_data = """4
baz.zi@nypc.co.kr
#dao#@.nexon._com
A@B@C
nexon.com"""

# 입력을 줄 단위로 나누기
lines = input_data.split('\n')

# 첫 번째 줄은 테스트 케이스의 수
num_cases = int(lines[0])

# 각 테스트 케이스를 확인하고 결과 출력
results = []
for i in range(1, num_cases + 1):
    email = lines[i]
    results.append(is_valid_email(email))

# 결과 출력
for result in results:
    print(result)
```
