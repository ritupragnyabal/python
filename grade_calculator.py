grade = float(input("Enter your grade: "))
if grade == 100:
    print("You have received an O grade.")
elif grade >= 90 and grade < 100:
    print("You have received an A grade.")  
elif grade >= 80 and grade < 90:
    print("You have received a B grade.")
elif grade >= 70 and grade < 80:
    print("You have received a C grade.")
elif grade >= 60 and grade < 70:
    print("You have received a D grade.")
elif grade >= 50 and grade < 60:
    print("You have received an E grade.")
elif grade < 50:
    print("You have received an F grade.")
else:
    print("Invalid grade entered.")