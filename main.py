import random
code_symbols = ('+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890')
code = ''
length = int(input('какая длина пароля?'))
for i in range (length):
    code += random.choice(code_symbols)
print(code)

