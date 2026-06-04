
'''
✅ Task21
Matnni kichik harfga o‘tkazing va ‘python’ so‘zi borligini tekshiring

Input	                    Output
"Men PYTHONni yoqtiraman"	True
"Java afzal"	            False
'''

text = input("Matnni kiriting: ")
low = text.lower()
result = 'python' in low
print(result)