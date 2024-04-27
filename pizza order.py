size=input("enter your size:")
bill=0
if size=="small":
    bill+=150
elif size == "large":
        bill +=200
else:
    bill +=250
add_pepperoni = input("do you want pepperoni")
if add_pepperoni=="yes":
    bill+=3
extra_cheese= input("do you want extre cheese")
if extra_cheese == "yes":
    bill +=4
print(f"your final bill is {bill}rs")




