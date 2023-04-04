import random

choice = input("Choose Rock, Papper or Scissors \n")

print("You :", choice.lower())

if choice.lower() == 'rock':
  print("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

  """)

elif choice.lower() == "papper":
  print("""
  
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)

  """)


elif choice.lower() == "scissors":
  print("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

  """)

else:
  print("Please enter a valid input...")


dict_choice = ["Rock","Papper","Scissors"]

comp_choice = dict_choice[random.randint(0,(len(dict_choice)-1))]
print(comp_choice)


if comp_choice.lower() == 'rock':
  print("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

  """)

elif comp_choice.lower() == "papper":
  print("""
  
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)

  """)


elif comp_choice.lower() == "scissors":
  print("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

  """)

else:
  print("I am not able to think")




if choice.lower() == "rock" and comp_choice.lower() == "rock":
  print("It's a Draw")

elif choice.lower() == "rock" and comp_choice.lower() == "papper":
  print("You Loose, Computer Won")

elif choice.lower() == "rock" and comp_choice.lower() == "scissors":
  print("You Won")

elif choice.lower() == "papper" and comp_choice.lower() == "rock":
  print("You Won")

elif choice.lower() == "papper" and comp_choice.lower() == "papper":
  print("It's a Draw")

elif choice.lower() == "papper" and comp_choice.lower() == "scissors":
  print("You Loose, Computer Won")


elif choice.lower() == "scissors" and comp_choice.lower() == "rock":
  print("You Loose, Computer Won")

elif choice.lower() == "scissors" and comp_choice.lower() == "papper":
  print("You won")

elif choice.lower() == "scissors" and comp_choice.lower() == "scissors":
  print("It's a Draw")

else:
  print("System is crashed")