import random
import string

def generate_password(length):
    #add all the letters, number, puntuation 
    char = string.ascii_letters + string.digits + string.punctuation

    #pick random character from char based on the length
    password = ''.join(random.choice(char)for _ in range(length))

    return password 

length = int(input("input Password length? \n"))
print (f"Password : {generate_password(length)}")