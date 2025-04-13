from nltk.corpus import words
import random

# 先创建一个列表，让nltk随机给一个单词
# 单词展示给用户看，猜测机会是单词个数*1.25倍
# 如果猜对，继续踩踩
words_storage = words.words()

generate_random_word = random.choice(words_storage)

print(generate_random_word)
