
'''
✅ Task14
Ikkita matn o'qilganda bir qil yoki yo'qligini tekshiring

Input	            Output
"salom", "salom"	True
"SALOM", "salom"	True
"hello", "salom"	False
'''

text1 = input("Birinchi matnni kiriting: ")
text2 = input("Ikkinchi matnni kiriting: ")

text1 = text1.lower()
text2 = text2.lower()

if text1 == text2:
    print("True")
else:
    print("False")