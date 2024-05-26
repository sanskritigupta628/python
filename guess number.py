import random
level=input("type 'easy' or 'hard':")
if level=="easy":
    attempt=10
else:
    attempt=5
c=random.randint(1,100)
for i in range(attempt):
 a=int(input("enter a no."))
 if a==c:
    print("ur right!")
    break
 else:
    print("ur wrong!")
    if a>c:
       print("too high")
    else:
          print("too low")
    attempt=attempt-1
    if attempt!=0:
       print(f"attempt left are {attempt}")
    else:
       print("ur out of attempt")
       print(f"the ans was {c}")


   
