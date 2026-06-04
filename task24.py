
'''
✅ Task24 – Email tekshiruv (Django user auth dan ilhomlangan)
Foydalanuvchining email manzili @ bilan boshlanmasligi va .com bilan tugashini tekshiring

Input	Output
"user@example.com"	True
"@example.com"	False
"user@example.net"	False
'''

email = input("Enter your email: ")
if email.endswith(".com") and not email.startswith("@"):
    print(True)
else:
    print(False)