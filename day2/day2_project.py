print('welcome to the tip calculator!')

total_bill = float(input('what is the total bill? $:'))

tip = int(input('how much tip would you like to give? 10,12 or 15?\n'))

person = int(input('how many people spilt the bill?\n'))

cal_money = (total_bill+(total_bill*(tip/100)))/person
# f函数把所有类型都换成字符串 类型转换 int float boolean str
print(f'each person should pay :{cal_money:.2f}$')
print(f'each person should pay :{round(cal_money)}$')
