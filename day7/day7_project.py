from nltk.corpus import words
import random

world_list = words.words()

random_world = random.choice(world_list)

print(random_world)
display_word = len(random_world) * "_"

print(
    f"world to guess:{display_word} ({len(random_world)}letters),you have {len(random_world) * 1.25:.0f} chances!")
length = round(len(random_world) * 1.25)
for attempt in range(length):
    current_chance = input(f"the {attempt+1} guess,Guess a letter: ")
    if current_chance in random_world:
        print('congratulation! you\'ve guess one word!')
    else:
        print('wrong! you use all the chance')
