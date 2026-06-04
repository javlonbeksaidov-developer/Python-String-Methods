
'''
✅ Task27 – Document type aniqlash (Linux file command ilhomida)
Fayl nomi .pdf, .docx, yoki .txt bilan tugashini tekshiring

Input	Output
"report.pdf"	True
"photo.jpeg"	False
'''

file = input("Enter file name: ")
if file.endswith(".txt") or file.endswith(".docx") or file.endswith(".pdf"):   
    print(True)
else:
    print(False)