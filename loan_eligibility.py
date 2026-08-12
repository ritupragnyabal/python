age = int(input("Enter your age: "))
salary = float(input("Enter your salary: "))
if age >= 60:
    if salary >= 50000:
        print("You are eligible for a loan.")
    else:
        print("You are not eligible for a loan due to insufficient salary.")
else:
    print("You are not eligible for a loan due to age restrictions.")