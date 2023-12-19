#this is a game that uses randomisation, from a dice that rolls 0-1
import random

random_side = random.randint(0, 1)
if random_side == 1:
  print("Heads")
else:
  print("Tails")

