'''print(3*3+3/3-3)
print(3*(3+3)/3-3)'''

#bmi calculation
#bmi calculation
height = input("enter your height in cm")
weight = input("enter your weight")

weight_as_int = int(weight)
height_as_float = float(height)
bmi = weight_as_int / (height_as_float * height_as_float)
if bmi<18.5:
    print(f"your bmi is{bmi},you are underage")
elif bmi<25:
    print(f"your bmi is{bmi},you have normal weight")
elif bmi<30:
    print(f"your bmi is{bmi},you are slightly overweight")
elif bmi<35:
    print(f"your bmi is{bmi},you are obese")
else:
    print(f"your bmi is{bmi},you are clinically obese")
