### if문과 정규식을 사용한 버전

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



### 정규식만을 사용한 버전
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
