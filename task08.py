
'''
✅ Task08
Matn ma’lum so‘z bilan boshlanishini tekshiring

Input	            Output
"Hello world",      "Hello"	True
"Hi there",         "Hello"	False
'''

text = input("Matnni kiriting: ")
start = input("Matn qaysi so'z bilan boshlanishi kerak? ")
result = text.startswith(start)
print(result)