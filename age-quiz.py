age = input("Enter your age: ")
user_age = int(age)
if user_age < 13:
    print("You qualify for the kiddie discount.")
elif user_age == 21:
    print("Congrats on your 21st!")
elif user_age >= 40:
    print("You're over the hill.")
elif user_age >= 65:
    print("Enjoy your retirement!")
elif user_age > 100:
    print("Sorry, you're dead.")
else:
    print("Age is but a number.")