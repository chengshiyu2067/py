# 38

# fruits = ['apple', 'peach', 'pear']

# for fruit in fruits:
#     print(fruit)
#     print(fruit + ' pie')
# print(fruits)

# 39

score = [108, 51, 121, 88, 65, 58, 133, 60, 108, 141, 99]
# total = 0
# for each_score in score:
#     total += each_score
#     print(f"now is {total}")
# total_score = sum(score)
# print(total_score)

# print(total)
# high_score = 0
# for each_score in score:
#     if each_score > high_score:
#         high_score = each_score
#         print(high_score)
#     else:
#         continue
# print(high_score)
# high_score = max(score)
# print(high_score)


# 40

# range 左闭右开
# test = list(range(0, 20, 2))

# print(test)

# for number in range(0, 11):
#     print(number)

# sum_gaosi = 0
# for gaosi in range(1, 101):
#     sum_gaosi += gaosi
# print(sum_gaosi)

# gaosi2 = sum(range(1, 101))
# print(gaosi2)

# practise
for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        number = 'FizzBuzz'
        print(number)
    elif number % 3 == 0:
        number = 'Fizz'
        print(number)
    elif number % 5 == 0:
        number = 'Buzz'
        print(number)
    else:
        print(number)
