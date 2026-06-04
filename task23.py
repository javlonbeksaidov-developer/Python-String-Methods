
'''
✅ Task23
Matnni upper qilgach, faqat katta harflardan iboratligini tekshiring

Input	    Output
"hello"	    True
"Hello"	    True
'''

text = input("Matnni kiriting: ")
up = text.upper()
result = up.isupper()
print(result)