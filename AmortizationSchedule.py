import matplotlib.pyplot as plt

# Define loan parameters
loan_amount = 275000
down_payment = 0.05*loan_amount
loan_term = 30 # in years
interest_rate = 0.07 # Interest Rate

# Calculate monthly payment
num_payments = loan_term * 12
principal = loan_amount - down_payment
monthly_rate = interest_rate / 12
monthly_payment = (monthly_rate * principal) / (1 - (1 + monthly_rate) ** (-num_payments))

# Generate amortization schedule
balance = principal
payments = []
for i in range(num_payments):
    interest_payment = balance * monthly_rate
    principal_payment = monthly_payment - interest_payment
    balance = balance - principal_payment
    payments.append((i+1, principal_payment, interest_payment, balance))

# Print amortization schedule
int_total = 0
for payment in payments:
    # print("{}\t${:,.2f}\t${:,.2f}\t${:,.2f}".format(payment[0], payment[1], payment[2], payment[3]))
    int_total = payment[2] + int_total


print("Monthly payment: ${:,.2f}".format(monthly_payment))
print("Total Intrest: ${:,.2f}".format(int_total))
print("Total Payment: ${:,.2f}".format(int_total+loan_amount))
print()


