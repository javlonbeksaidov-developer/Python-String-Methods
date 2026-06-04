
'''
✅ Task03
Matnda faqat harf yoki raqamdan iboratligini tekshiring

Input	    Output
"Python3"	True
"Python 3"	False
'''

text = input("Matnni kiriting: ")
result = text.isalnum()
print(result)