
'''
✅ Task07
Matn ma’lum so‘z bilan tugashini tekshiring

Input	            Output
"Hello world",      "Hello"	False
"Hi there",         "there"	True
'''

text = input("Matnni kiriting: ")
end = input("Matn qaysi so'z bilan tugashi kerak? ")
result = text.endswith(end)
print(result)