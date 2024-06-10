import random
card=['a', '2' , '3', '4', '5', '6', '7' ,'8', '9', '10', 'j', 'q', 'k']
print(card)
random.shuffle(card)
print(card)
print(random.choice(card))