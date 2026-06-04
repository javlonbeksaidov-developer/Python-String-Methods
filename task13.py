
'''
✅ Task13
Ikkita matn kiritiladi birinchisi ikkinchisida bor yoki yo'qligini aniqlash

Input	    Output
"salom",    "salom dunyo"	True
"SALOM",    "salom dunyo"	True
"hello",    "salom dunyo"	False
'''

text1 = input("Birinchi matnni kiriting: ")
text2 = input("Ikkinchi matnni kiriting: ")

text1 = text1.lower()
text2 = text2.lower()

if text1 in text2:
    print("True")
else:
    print("False")