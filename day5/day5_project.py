import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
           'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("welcome to the pypassword generator!")

need_letters = int(
    input('how mant letters would you like in your password?\n'))
need_symbols = int(
    input('how mant symbols would you like in your password?\n'))
need_numbers = int(
    input('how mant numbers would you like in your password?\n'))

# print(need_letters)
# print(need_symbols)
# print(need_numbers)

new_letters = random.choices(letters, k=need_letters)
new_symbols = random.choices(symbols, k=need_symbols)
new_numbers = random.choices(numbers, k=need_numbers)

print(new_letters, new_symbols, new_numbers)

total_chars = ''.join(new_letters)+''.join(new_symbols) + ''.join(new_numbers)

print(total_chars)  # simple version

passwd = list(total_chars)
# 打乱顺序 shuffle只能原地打乱数组列表，不能打乱字符串
random.shuffle(passwd)
passwd = ''.join(passwd)
print(passwd)  # hard version
