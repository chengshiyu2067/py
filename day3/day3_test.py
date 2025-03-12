# number = int(input('select one number and tell me\n'))

# if number > 50:
#     print('your number is large than 50')
# else:
#     print('your number is smaller than 50')


# modulo = 10 % 3

# print(modulo)

total_bill = 0

print('welcome to the pizza deliveries!')

size = input('what size do you want? s? m or l\n')

pepperoni = input('do you want pepperoni on your pizza?\n')

extra_cheese = input('do you want extra cheese y or n?\n')

# if size == "s":
#     total_bill += 15
#     if pepperoni == 'y':
#         total_bill += 2
#     if extra_cheese == 'y':
#         total_bill += 1

# elif size == "m":
#     total_bill += 20
#     if pepperoni == 'y':
#         total_bill += 3
#     if extra_cheese == 'y':
#         total_bill += 1
# elif size == "l":
#     total_bill += 25
#     if pepperoni == 'y':
#         total_bill += 3
#     if extra_cheese == 'y':
#         total_bill += 1
if size == 's':
    total_bill += 15
elif size == 'm':
    total_bill += 20
elif size == 'l':
    total_bill += 25
else:
    print('please select the correct option')

if pepperoni == 'y':
    if size == 's':
        total_bill += 2
    else:
        total_bill += 3

if extra_cheese == 'y':
    total_bill += 1
print(f'you need to pay {total_bill}$')
