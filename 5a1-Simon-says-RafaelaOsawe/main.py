import random
from random import choice
from random import randint
from time import sleep

simon_says = ["Hands on head", "Hands on ears",
              "Right hand up", "Left hand up",
              "Hands on shoulders"]
intros =  ["Simon says...",""]

for instructions in range (1, 11):
  index = randint(0, 4)
  instruction = simon_says[index]
  intro = choice(intros)
  print(intro,instruction)
  sleep(3)

keyboard_input = ["a", "b", "c", "d", "1", "2"]
intros_keyboard =  ["Simon says press...","Press"]
points = 0

print("We are now going to be playing Simon Says with a keybaord twist!")

while user_input == True:
  index = randint(0, 5)
  intro_keyboard = choice(intros_keyboard)
  print(intro_keyboard+keyboard_input)
  user_input = ""
  if user_input == keyboard_input and intros_keyboard == "Simon says press..."
    print



