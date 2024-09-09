import random
options = ["Rock","Paper","Scissor"]
def rock_paper_scissor():
    print("Welcome To Rock Paper Scissor Game!!!")
    print("Your Opponent Will be Mr.MUTERIX")
    print("Options Available :- Rock,Paper,Scissor")
    print("RULES OF GAME:-")
    print("Unexpected Behaviour Will kill the game!!!")
    print("1.First To Score 10 points will win!!")
    print("2.Rock vs. Paper: Paper wins.\n3.Rock vs Scissor: Scissor Wins\n4.Paper Vs Scissor: Scissor wins")
    print("COMMAND INSTRUCTIONS:-")
    print("S -> For Start\nE -> For End\nC -> Check Score")
    control = True
    user_score = 0
    computer_score = 0
    while control:
        if((user_score==10)or(computer_score==10)):
            if(user_score==10):
                print("Congratulations!!!")
                print("You Win")
                return
            else:
                print("SORRY")
                print("MR. MUTERIX wins!!!")
                print("Better Luck Next Time!!")
                return
        user_command = input("Enter Your Command: ")
        if(user_command=="E"):
            print("\nKilling the Game.....")
            break
        elif(user_command=="C"):
            print("\nMR. MUTERIX'S SCORE ->",computer_score)
            print("Your Score ->",user_score)
        elif(user_command=="S"):
            user_choice = input("\nYour Choice: ")
            computer_choice = random.choice(options)
            print("MR. MUTERIX Choice ->",computer_choice)
            if((user_choice=="Paper")and(computer_choice=="Rock")):
                print("You Got 1 point.")
                user_score+=1
            elif((user_choice=="Rock")and(computer_choice=="Paper")):
                print("MUTERIX Got 1 point.")
                computer_score+=1
            elif((user_choice=="Scissor")and(computer_choice=="Paper")):
                print("You Got 1 point.")
                user_score+=1
            elif((user_choice=="Paper")and(computer_choice=="Scissor")):
                print("MUTERIX Got 1 point.")
                computer_score+=1
            elif((user_choice=="Rock")and(computer_choice=="Scissor")):
                print("You Got 1 point.")
                user_score+=1
            elif((user_choice=="Scissor")and(computer_choice=="Rock")):
                print("MUTERIX Got 1 point.")
                computer_score+=1
            elif((user_choice==computer_choice)):
                print("Its A Draw!!")
                print("Both Will Get No point")
                user_score+=0
                computer_score+=0
            else:
                print("Inavlid Input!!!")
                continue
        else:
            print("Invalid Statement!!!")
            print("Try Again!!!")
            continue
