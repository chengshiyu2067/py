print('''                                   88             
                                   88             
                                   88             
,adPPYYba, 8b,dPPYba,  8b,dPPYba,  88  ,adPPYba,  
""     `Y8 88P'    "8a 88P'    "8a 88 a8P_____88  
,adPPPPP88 88       d8 88       d8 88 8PP"""""""  
88,    ,88 88b,   ,a8" 88b,   ,a8" 88 "8b,   ,aa  
`"8bbdP"Y8 88`YbbdP"'  88`YbbdP"'  88  `"Ybbd8"'  
           88          88                         
           88          88         
''')
print('welcome to treasure island.your mission is to find the treasure')

direction_choose = input(
    'your are at a cross road, where do you want to do?\n type left or right\n').lower()

if direction_choose in ['left', 'l']:
    swim_choose = input(
        "you come to a lake\n choose swim to cross the lake or choose wait to wait the boat\n").lower()
    if swim_choose in ['wait', 'w']:
        door_choose = input(
            'now,you come to three doors,choose one,red,yellow or blue\n').lower()
        if door_choose in ['red', 'r']:
            print('burned by fire.game over')
        elif door_choose in ['blue', 'b']:
            print('eaten by beasts. game over')
        elif door_choose in ['yellow', 'y']:
            print('you win!')
        else:
            print('game over!')
    else:
        print('attacked by trout. game over')
else:
    print('fall into a hole. game over!')
