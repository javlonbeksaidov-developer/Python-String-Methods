
'''
✅ Task22
Bo‘sh joylarni olib tashlab, satr bo‘sh emasligini tekshiring

Input	    Output
"     "	    False
"Hello "	False
'''

text = input("Matnni kiriting: ")
empty_space = text.replace(" ", "")
result = bool(empty_space)
print(result)
