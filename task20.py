
'''
✅ Task20
Matnning faqat birinchi harfini katta qilib, bosh harf bilan boshlanganini tekshiring

Input	            Output
"python darslari"	False
"Python darslari"	True
'''

text = input("Matnni kiriting: ")
first_char = text[0]
result = first_char.isupper()
print(result)