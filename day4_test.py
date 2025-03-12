import random
# 创建自己的模块
import my_module

# randomint = random.randint(1, 5)
# random_number_0to1 = random.random()
# random_number_0to10 = random.random() * 10
# random_float = random.uniform(1, 10)
# # print(randomint)
# # print(my_module.my_favourite_number)

# # print(f"{random_number_0to10:.2f}")

# print(f"{random_float:.2f}")

# number = random.randint(0, 1)

# if number == 1:
#     print(f"the number is {number},Heads!")
# elif number == 0:
#     print(f"the number is {number},Tails!")

states_of_america = ['delaware', 'pennsylvania', 'new jersey', 'georgia', 'connecticut', 'maine', 'vermont',
                     'new york', 'michigan', 'rhode island', 'wisconsin', 'minnesota', 'south dakota', 'north dakota', 'texas']

print(len(states_of_america))
# states_of_america[1] = 'pencilvania'
# # 数组追加
# states_of_america.append('angelaland')
# print(states_of_america)

friends = ['jack', 'tom', 'lily', 'lucy']
# option 1
# print(random.choice(friends))
# option 2
random_index = random.randint(0, 3)

print(friends[random_index])
print(my_module.my_favourite_number)

# 嵌套列表
states_of_china = ['shanghai', 'chengdu', 'beijing', 'hongkong']

city_of_states = [states_of_america, states_of_china]

# print(city_of_states)
print(city_of_states[1][1])
print(city_of_states[1])

# 索引解析：
# 第一个[1] → 取第二组城市列表（中国的states_of_china）
# 第二个[1] → 取中国列表中的第二个城市（索引从0开始）
