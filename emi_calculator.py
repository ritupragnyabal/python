principle_rate_amount = int(input("Enter the principal amount: "))
interest_rate = float(input("Enter the interest rate (in percentage): "))
time_period = float(input("Enter the time period (in years): "))
monthly_interest_rate = interest_rate / (12 * 100)
number_of_payments = time_period * 12

emi = (principle_rate_amount * monthly_interest_rate * (1 + monthly_interest_rate) ** number_of_payments) / ((1 + monthly_interest_rate) ** number_of_payments - 1)
print("The Equated Monthly Installment (EMI) is:", round(emi, 2))