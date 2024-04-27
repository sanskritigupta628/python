print("Welcome To Treasure island. Your mission is to find the treasure.")

value = input("Enter left or right: ")

if value == "right":
    print("Game over.")
else:
    print("You have stepped into level 2.")
    value1 = input("Do you want to swim or wait? There is a lake. ")

    if value1 == "swim":
        print("GAME OVER, loser.")
    elif value1 == "wait":
        print("You made a good decision. You've stepped into level 3.")

    value3 = input("There are three doors: red, blue, and yellow. Choose one: ")

    if value3 == "red" or value3 == "blue":
        print("You made a bad decision. Game over.")
    elif value3 == "yellow":
        print("Congratulations! You are the winner of the game.")
    else:
        print("You are not in the list. You stepped out of the game.")
final codeee