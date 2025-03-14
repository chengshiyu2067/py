import random

option = ['rock', 'paper', 'scissor']
User_input = int(input(
    'what do you choose? type 0 for rock,type 1 for paper type 2 for scissors\n'))

User_choose = option[User_input]

print(f'you choose {User_choose}!')

computer_input = random.randint(0, 2)

computer_choose = option[computer_input]

if (User_input - computer_input) % 3 == 0:
    print(f'the compuer choose {computer_choose},its a draw!')

elif (User_input - computer_input) % 3 == 2:
    print(f'the compuer choose {computer_choose},you lose!')

else:
    print(f'the compuer choose {computer_choose},you win!')

# 这种将循环关系映射到数轴上的方法，可以推广到任意N个元素的循环博弈场景（使用模N运算）
# rock 0
# paper 1
# scissors 2
# user loose -1 -1 2
# 2 % 3 = 2    # 3*0=0，余2（被除数小于除数时，余数=被除数）
# -1 % 3 = 2   # 负数运算：-1 + 3 = 2
# test = 2 % 3
# print(test)
