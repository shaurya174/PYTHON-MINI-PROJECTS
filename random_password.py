import random
def password_maker(length):
    user_password=""
    characters = [
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 
    '!', '@', '#', '$', '%', '&', '*']
    i = 1
    while(i<=length):
        user_password = user_password+random.choice(characters)
        i = i + 1
    return user_password
user_length = int(input("Enter Length Of Password: "))
user_password = password_maker(user_length)
print("Your Custom Generated Password:",user_password)

