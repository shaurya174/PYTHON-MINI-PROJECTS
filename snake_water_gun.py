import random
options = ["Snake","Water","Gun"]
def snake_water_gun():
    print("Welcome To Snake Water Gun Game!!!")
    print("Your Opponent Will be Mr.NOOB MASTER69")
    print("Options Available :- Snake,Water,Gun")
    print("RULES OF GAME:-")
    print("Unexpected Behaviour Will kill the game!!!")
    print("1.First To Score 10 points will win!!")
    print("2.Snake vs. Water: Snake drinks the water hence wins.\n3.Water vs. Gun: The gun will drown in water, hence a point for water\n4.Gun vs. Snake: Gun will kill the snake and win.")
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
                print("MR. NOOB MASTER69 wins!!!")
                print("Better Luck Next Time!!")
                return
        user_command = input("Enter Your Command: ")
        if(user_command=="E"):
            print("\nKilling the Game.....")
            break
        elif(user_command=="C"):
            print("\nNOOB MASTER69 ->",computer_score)
            print("Your Score ->",user_score)
        elif(user_command=="S"):
            user_choice = input("\nYour Choice: ")
            computer_choice = random.choice(options)
            print("NOOB MASTER69 Choice ->",computer_choice)
            if((user_choice=="Snake")and(computer_choice=="Water")):
                print("You Got 1 point.")
                user_score+=1
            elif((user_choice=="Water")and(computer_choice=="Snake")):
                print("NOOB MASTER69 Got 1 point.")
                computer_score+=1
            elif((user_choice=="Water")and(computer_choice=="Gun")):
                print("You Got 1 point.")
                user_score+=1
            elif((user_choice=="Gun")and(computer_choice=="Water")):
                print("NOOB MASTER69 Got 1 point.")
                computer_score+=1
            elif((user_choice=="Gun")and(computer_choice=="Snake")):
                print("You Got 1 point.")
                user_score+=1
            elif((user_choice=="Snake")and(computer_choice=="Gun")):
                print("NOOB MASTER69 Got 1 point.")
                computer_score+=1
            elif((user_choice==computer_choice)):
                print("Its A Draw!!")
                print("Both Will Get 1 point")
                user_score+=1
                computer_score+=1
            else:
                print("Inavlid Input!!!")
                break
        else:
            print("Invalid Statement!!!")
            print("Killing Game....")
            break
snake_water_gun()