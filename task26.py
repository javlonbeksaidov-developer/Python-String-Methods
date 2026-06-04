
'''
✅ Task26 – GitHub username validatsiyasi
GitHub usernames faqat a-z, A-Z, 0-9, - dan iborat bo‘lishi kerak, isalpha() bilan tekshirishdan oldin replace("-", "") bilan - belgilarini olib tashlang.

Input	Output
"ali-coder"	True
"diyor_123"	False
'''

username = input("Enter username: ")
username = username.replace("-", "")
username = username.isalnum()
print(username)