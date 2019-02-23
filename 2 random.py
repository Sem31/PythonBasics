# Random no. function

import random

#choice

print("random no. from 0 to 100 = ",random.choice(range(100)))

list = [1,2,8,7,9,10]
print("Random no. from list = ",random.choice(list))

str = "Hello Sem"
print("random no. from the string =",random.choice(str))

#randrange

print("randrange func(0,100,2) = ",random.randrange(0,100,2))
print("randrange func(100) = ",random.randrange(100))

#random

print("only use random see first random = ",random.random())
print("only use random see Second random = ",random.random())

#seed

random.seed()
print("seed function = ",random.random())

#shuffle()

list = [10,2,5,4,8,9,6]
random.shuffle(list)
print("shuffle () used : ", list)

#uniform ()

print("uniform (5,10) : ",random.uniform(5,10))








