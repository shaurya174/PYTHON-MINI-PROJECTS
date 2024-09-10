import random
import time
outcomes = [1,2,3,4,5]
def win(user_list,computer_list):
    if((user_list[0]==user_list[1])and(user_list[0]==user_list[2])):
        return True
    for j in range(3):
        if(user_list[j]!=computer_list[j]):
            return False
    return True
def print_outcome(n):
    if(n==1):
        print("\U0001F34B",end=" ",flush=True)
    elif(n==2):
        print("\U0001F34A",end=" ",flush=True)
    elif(n==3):
        print("\U0001F352",end=" ",flush=True)
    elif(n==4):
        print(" 7️⃣",end=" ",flush=True)
    elif(n==5):
        print("\U0001F514",end=" ",flush=True)
def print_reel(a,b,c):
    print("Spinning.......")
    print("\n\n")
    time.sleep(3)
    print_outcome(a)
    time.sleep(3)
    print("|",end=" ",flush=True)
    time.sleep(3)
    print_outcome(b)
    time.sleep(3)
    print("|",end=" ",flush=True)
    time.sleep(3)
    print_outcome(c)
def slot_machine():
    print("---------------Welcome To Slot Machine----------------")
    print("                     RULES OF PLAY                     ")
    print("YOU HAVE TO FIRST INPUT MONEY!!!")
    print("YOU CAN PLAY AS MANY ROUNDS AS YOU WANT UNTIL YOUR MONEY IS OVER.")
    print("(i)   If win: Money will be Doubled which is spent on that round")
    print("(ii)  If lose: Money will be deducted which is spent on that round")
    print("\n\n\n")
    print("*******************Winning Conditions********************")
    print("(i)   Same Symbols Shown On Three Reels On Your Chance")
    print("(ii)  Same Combination On your chance and on computer's choice.")
    print("(iii) Symbols For Game:")
    print("      1. Lemon  -> \U0001F34B")   # 🍋 Lemon
    print("      2. Orange -> \U0001F34A")   # 🍊 Orange
    print("      3. Cherry -> \U0001F352")   # 🍒 Cherry
    print("      4. Seven  -> 7️⃣")          # Seven
    print("      5. Bell   -> \U0001F514")   # 🔔 Bell
    user_balance = int(input("Enter Your Balance: "))
    gained_amount = 0
    loss_amount = 0
    i = 1
    while True:
        user_choice = input("Do You Want To Spin For Round (Y/N) "+str(i)+": ")
        if(user_balance<=0):
            print("Out Of Money!!")
            break
        if(user_choice=='N'):
            print("Ok! Slot Time Over!!!")
            print("Here are the details of your balance: ")
            print("1. Available Balance: "+str(user_balance))
            print("2. Amount Gained: "+str(gained_amount))
            print("3. Amount Lost: "+str(loss_amount))
            break
        elif(user_choice=='Y'):
            i+=1
            round_amount = int(input("Amount You Want To Bet On This Round: "))
            while((round_amount<0)or(round_amount>user_balance)):
                print("Please Place Valid Bet")
                round_amount = int(input("Amount You Want To Bet On This Round: "))
            user_balance-=round_amount
            user_list=[]
            computer_list=[]
            for k in range(0,3):
                a = random.choice(outcomes)
                user_list.append(a)
                b = random.choice(outcomes)
                computer_list.append(b)
            print("User's Outcomes: ")
            print_reel(user_list[0],user_list[1],user_list[2])
            print("\nComputer's Outcomes: ")
            print_reel(computer_list[0],computer_list[1],computer_list[2])
            result = win(user_list,computer_list)
            if(result):
                print("\n")
                print("You Won This Round!!")
                user_balance+=(2*round_amount)
                print("Current Balance: "+str(user_balance))
            else:
                print("\n")
                print("Sorry!You Lost This Round.")
                print("Current Balance: "+str(user_balance))
        else:
            print("Invalid Choice!!")
            print("Try Again......")

slot_machine()