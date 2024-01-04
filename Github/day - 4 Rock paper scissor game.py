import random

def get_user_choice():
    while True:
        try:
            user_choice = int(input("Enter your choice (1 for rock, 2 for paper, 3 for scissors): "))
            if user_choice in [1, 2, 3]:
                return user_choice
            else:
                print("Invalid choice. Please enter 1 for rock, 2 for paper, or 3 for scissors.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def convert_to_gesture(choice):
    if choice == 1:
        return 'rock'
    elif choice == 2:
        return 'paper'
    elif choice == 3:
        return 'scissors'

def display_gesture(gesture):
    if gesture == 'rock':
        print("""
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
        """)
    elif gesture == 'paper':
        print("""
        _______
    ---'   ____)____
              ______)
              _______)
             _______)
    ---.__________)
        """)
    elif gesture == 'scissors':
        print("""
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
        """)

def get_computer_choice():
    return random.randint(1, 3)

def determine_winner(user, computer):
    if user == computer:
        return "It's a tie!"
    elif (user == 1 and computer == 3) or (user == 2 and computer == 1) or (user == 3 and computer == 2):
        return "You win!"
    else:
        return "Computer wins!"

def play_game():
    print("Let's play Rock-Paper-Scissors!")
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        
        print("\nYou chose:")
        display_gesture(convert_to_gesture(user_choice))
        print("\nComputer chose:")
        display_gesture(convert_to_gesture(computer_choice))
        
        result = determine_winner(user_choice, computer_choice)
        print("\n" + result)
        
        play_again = input("Do you want to play again? (y/n): ").lower()
        if play_again != 'y':
            print("Thanks for playing!")
            break


play_game()
