rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random
choice = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")
if choice == "0":
  print("you have selected rock\n" + (rock))
elif choice == "1":
  print("you have selected paper\n" + (paper))
elif choice == "2":
  print("you have selected scissors\n" + (scissors))

computer_choice = [rock, paper, scissors]
cc = random.choice(computer_choice)
print(f"computer's choice is {cc}")


if choice == "0" and cc == rock:
  print("That's a draw")
elif choice == "0" and cc == scissors:
  print("Rock beats Scissors; You win")
elif choice == "1" and cc == paper:
  print("That's a draw")
elif choice == "1" and cc == rock:
  print("Paper beats Rock; You win")
elif choice == "2" and cc == scissors:
  print("That's a draw")
elif choice == "2" and cc == paper:
  print("Scissors beats Paper; You win")
else:
  print("You lose")