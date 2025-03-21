# len函数只能算字符串长度
print(len(str(12345)))
# 输出字符串第几位字符
print("1234"[1])
print("hello"[4])
print('hello'[-1])
# check class
print(type(123))
print(type(True))
# 两个斜杠float边int 尽量不要用
print(6 // 3)
# 指数
print(2**5)
# round()四舍五入
bmi = 66 / 1.77 ** 2
print(round(bmi))
print(round(bmi, 2))

score = 0

score += 1

print(score)

# lower test
lower_test = input('typed something').lower()
print(lower_test)
