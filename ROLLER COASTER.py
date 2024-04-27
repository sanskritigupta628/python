print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))

    if age < 12:
        bill = 5
        print("Child tickets are rs5.")
    elif age >= 45 and age <= 55:
        bill = 0
        print("Old age tickets are free.")
    elif age <= 18:
        bill = 7
        print("Youth tickets are rs7.")
    elif age <= 30:
        bill = 12
        print("Adult tickets are rs12.")
    else:
        print("Invalid input")

    wants_photo = input("Do you want a photo taken? Y or N. ")
    if wants_photo == "Y":
        bill += 3

    print(f"Your final bill is rs{bill}")

else:
    print("Sorry, you have to grow taller before you can ride.")