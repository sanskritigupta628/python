import random

numbers = "0123456789"
otp = ""
leangth=int(input("Enter the length of OTP:"))
for _ in range(leangth):
    otp += random.choice(numbers)

print("Generated OTP:",otp)