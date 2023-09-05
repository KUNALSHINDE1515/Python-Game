import random

Lunky_number = random.randint(1,100)

user_input = int(input("Enter the number : "))

while Lunky_number != user_input:

    if user_input == Lunky_number:
         print("You won, congratulation")
    else:
       if user_input > Lunky_number:
        print("too Large, try again")
       elif user_input < Lunky_number:
            print("too small, try again")
    user_input = int(input("Enter NUmber :"))
         
        

