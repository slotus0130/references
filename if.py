import sys

password = "{NYPCc2019}"

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

print("valid")
