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
options = [rock, paper, scissors]
user_decision = int(input("What do you choose? For rock, press 0, for paper, press 1, and for scissors, press 2."))
if user_decision >= 3 or user_decision < 0:
  print("Your number is invalid, you lose the game.")
else:
  if user_decision == 0:
    print(options[0])
  elif user_decision == 1:
    print(options[1])
  elif user_decision == 2:
    print(options[2])

  #Computer needs to make a random decision of whether to choose rock, paper, or scissors.
  import random
  computer_choice = random.randint(0,2)
  
  if computer_choice == 0:
    #Computer chose rock
    print(f"Computer chose: {options[0]}")
    if user_decision == 0:
      #Both user and computer chose rock
      print("It is a draw. Both user and computer chose rock.")
    elif user_decision == 1:
      #User chose paper, computer chose rock. 
      print("The user won. User chose paper and computer chose rock. Paper covers rock.")
    elif user_decision == 2:
      #User chose scissors, computer chose rock. 
      print("The computer won. User chose scissors and computer chose rock. The rock smashed the scissors.")
      
  elif computer_choice == 1:
    #Computer chose paper
    print(f"Computer chose: {options[1]}")
    if user_decision == 0:
      #User chose rock, computer chose paper
      print("The computer won. User chose rock, computer chose paper. Paper covers rock.")
    elif user_decision == 1:
      #The user and computer both chose paper
      print("It is a draw. Both user and computer chose paper.")
    elif user_decision == 2:
      #The user chose scissors, the computer chose paper
      print("The user won. User chose scissors and computer chose paper. Scissors cuts paper.")
  
  elif computer_choice == 2:
    #Computer chose scissors
    print(f"Computer chose: {options[2]}")
    if user_decision == 0:
      #User chose rock, computer chose scissors
      print("The user won. User chose rock, computer chose scissors. Rock smashes scissors.")
    elif user_decision == 1:
      #The user chose paper, the computer chose scissors
      print("The computer won. User chose paper, computer chose scissors. Scissors cuts paper.")
    elif user_decision == 2:
      #The user chose scissors, the computer chose scissors
      print("It is a draw. Both user and computer chose scissors.")
