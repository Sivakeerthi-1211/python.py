#calculating BMI
weight = input()
height= input()
bmi = weight/(height**2)
#Displaying the bmi
print("your bmi is:",round(bmi,2))
#checking the bmi category
if bmi<18.5:
    print('your are underweight.')
elif 18.5 <= bmi<24.9:
    print("you have a normal weight.")
elif 25<=bmi<29.9:
    print("you are overweight")
else:
    print("you are obese")