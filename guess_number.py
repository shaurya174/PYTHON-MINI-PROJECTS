import random
def guess_no(start,end):
    req_int = random.randint(start,end)
    not_found = True
    while(not_found):
        user_guess = int(input("Enter Number: "))
        if(user_guess==req_int):
            print("You Got It Right!")
            break
        elif((user_guess<start)or(user_guess>end)):
            print("\nOut Of Range!!")
            print("Try Again...")
        elif(user_guess<req_int):
            print("\nYou guessed a smaller number.")
            print("Try Again...")
        elif(user_guess>req_int):
            print("\nYou guessed a bigger number.")
            print("Try Again....")
user_start = int(input("Enter Start: "))
user_end = int(input("Enter End: "))
guess_no(user_start,user_end)
