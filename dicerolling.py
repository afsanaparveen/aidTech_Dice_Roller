import random

def play_game():
    print("Welcome to dice rolling game!!!")
    print("you and opposite player roll the dice and highest will win the game")
    while True:
        input("Press Enter to roll the dice......!")
        player_1=random.randint(1,6)
        player_2=random.randint(1,6)
        print("Player1 rolled:",player_1)
        print("Player2 rolled:",player_2)
        if player_1>player_2:
            print("player-1 winned the game")
        elif player_2>player_1:
             print("player-2 winned the game")
        else:
            print("it's a Tie")
        play_again=input("want to play again? (yes/no):")
        if play_again.lower()!="y":
            break
        
    print("Thanks for playing!!!")
play_game()