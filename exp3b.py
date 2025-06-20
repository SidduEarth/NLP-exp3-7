import random
letters = "abcdefghijklmnopqrstuvwxyz"
for i in range(5):
    length = random.randint(5, 10)
    word = "".join(random.choice(letters) for j in range(length))
    print("Random Word:", word)


