
'''
✅ Task19
Matnni kichik harflarga o‘tkazing va faqat raqamlardan iborat emasligini tekshiring

Input	    Output
"HELLO123"	False
"HELLO"	    True
'''

text = input("Matnni kiriting: ")
low = text.lower()
result = low.isalpha()
print(result)