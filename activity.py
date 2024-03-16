# Ask the user to input their age 
age = int(input("Enter your age:"))

# Ask the user intput whether they are a student or not
student_status = input("Are you a student? (yes/no):")

# use logical operators to determine if the person is eligible for a discount
if age <= 12:
    print ("you are eligible for a discount.")
elif age >= 13 and age <=18 and student_status == "yes":
    print("You are eligible for a discount.")
else:
    print("You are not eligible for a discount.")
