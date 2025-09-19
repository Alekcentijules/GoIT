# To get a random integer from a uniform distribution in the interval between a and b inclusive, 
# use the random.randint(a, b) method. It returns a random integer N such that a <= N <= b
# This method, for example, is suitable for simulating a dice roll:
import random

dice_roll = random.randint(1, 6)
print(f"You have given up {dice_roll}")



# The random.random() method is needed to get a random number in the interval 0, 1. 
# It generates a random real number between 0.0 (inclusive) and 1.0 (exclusive):
import random

num = random.random()
print(f"\nrandom.random(): {num}")



# Let's say you need to simulate a random percentage fill. You can use random.random() to do this:
import random

fill_percentage = random.random() * 100
print(f"\nfill_percentafe: {fill_percentage:.2f}%")



# The random.range(start, stop[, step]) method returns a randomly selected number from the specified range.
# For example, a simulation of a shot at a target, but you need to choose a random number from 1 to 10, and only odd numbers:
import random

target = random.randrange(1, 11, 2)
print(f"\nTarget: {target}")



# When you have a list of objects and you need to shuffle the order of the items in this list to a random order, 
# we use the random.shuffle(x) method, where x is the list you want to shuffle.
# Shuffling a deck of cards:
import random

cards = ["Ace", "King", "Qeen", "Jack", "10", "9", "8", "7", "6"]
random.shuffle(cards)

print(f"\nMixed deck: {cards}")



# If you want to select a random item from a list, you need to use the random.choice(seq) method, 
# where seq is the sequence to select: a list or a tuple.
# Selecting a random fruit:
import random

fruits = ["bamboo", "aplaz", "picklez"]
print(f"\nFruit: {random.choice(fruits)}")



# To select more than one random item from the list, we need the random.choices() method. 
# It is used to generate a random sample from a sequence. This method can return one or more items from the specified sequence, 
# while allowing for repetition of items in the sample.
import random

fruits = ["bamboo", "aplaz", "picklez", "panpineapleaplepan"]
chosen_fruits = random.choices(fruits, k=9)

print(f"\nchosen_fruits: {chosen_fruits}")



# Choice with scales:
import random

fruits = ["bamboo", "aplaz", "picklez", "panpineapleaplepan"]
weights = [3, 11, 10000, 10000000000]
chosen_fruits = random.choices(fruits, weights, k=5)

print(f"\nchosen_fruits_with_weights: {chosen_fruits}")



# If you need to select N elements from the list and they are not repeated, you should use the random.sample(population, k) 
# method. It returns a list of length k with unique elements selected at random from the population.
#  Creating a random team of 4 members from a group of 10 people:
import random

participants = ["a", "b", "c", "d", "e", "f", "g"]
team = random.sample(participants, 5)

print(f"\nParticipants: {team}")



# The last useful method to consider is random.uniform(a, b). The method returns a random real number N such that a <= N <= b.
# An example of generating a random price for a product in the range from 50 to 100:
import random

price = random.uniform(50, 100)
print(f"\nPrice of fruits: {price:.2f}")