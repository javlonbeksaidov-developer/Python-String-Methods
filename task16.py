
'''
✅ Task16
Matn ichidagi so‘zlarni almashtiring

Input	                            Output
"Salom dunyo", "dunyo", "olam"	    Salom olam
'''

text = input("Matnni kiriting: ")
old_word = input("Almashtirish uchun so'zni kiriting: ")
new_word = input("Yangi so'zni kiriting: ")
result = text.replace(old_word, new_word)
print(result)