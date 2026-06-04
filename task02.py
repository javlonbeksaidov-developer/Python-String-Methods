
'''
✅ Task02
Matn faqat raqamlardan iboratligini tekshiring

Input	    Output
"2025"	    True
"20y25"	False
'''

text = input("Matnni kiriting: ")
result = text.isdigit()
print(result)