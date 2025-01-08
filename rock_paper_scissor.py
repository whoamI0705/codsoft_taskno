import random

#function to play game, with score being tracked down
def rock_paper_scissor():
        user_choice = int(input("Type 0 for rock, 1 for paper and 2 for scissor:"))
        computer_choice = random.randint(0,2)
        if user_choice == computer_choice:
            print(f"Its a draw. Both the computer and the user chose {choices[user_choice]}.\n Final score:-\nPlayer Score: {score['usr']}   Computer Score: {score['comp']}")
            
        
        elif user_choice == 2 and computer_choice == 0:
            score["comp"]+= 1
            print(f"Computer wins! Computer chooses {choices[computer_choice]} while user chose {choices[user_choice]}.\n Final score:-\nPlayer Score: {score['usr']}   Computer Score: {score['comp']}")
            
            
        elif user_choice == 0 and computer_choice == 2:
            score["usr"] += 1
            print(f"User wins! Computer chooses {choices[computer_choice]} while user chose {choices[user_choice]}.\n Final score:-\nPlayer Score: {score['usr']}   Computer Score: {score['comp']}")
            
        elif user_choice > computer_choice:
            score["usr"] += 1
            print(f"User wins! Computer chooses {choices[computer_choice]} while user chose {choices[user_choice]}.\n Final score:-\nPlayer Score: {score['usr']}   Computer Score: {score['comp']}")
            
        else:
            score["comp"] += 1
            print(f"Computer wins! Computer chooses {choices[computer_choice]} while user chose {choices[user_choice]}.\n Final score:-\nPlayer Score: {score['usr']}   Computer Score: {score['comp']}")
            
     
print("Welcome to the rock,paper and scissor game!")
choices = ["rock", "paper", "scissor"]
score = {
    "usr" : 0,
    "comp" : 0}
play = input("Hit enter to begin! or Enter any other key to quit the game!")

if play == "":
    isPlay = True
    #while loop, to continue to play if user wants to play again
    while isPlay:
        rock_paper_scissor()
        print("\n")
        play_again = input("Do you wanna play again?\nType 'y' for yes or hit enter to play again or enter any other key to exit! ")
        if play_again == 'y' or play_again == "":
             isPlay = True
        else:
             print(f"Thanks for playing the game! Hope you enjoyed it!\n Final Score:- {score['usr']}(Player) / {score['comp']}(Computer)")
             isPlay = False


else:
     exit()
       


