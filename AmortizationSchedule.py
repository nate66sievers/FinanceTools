import matplotlib.pyplot as plt

# Define loan parameters
loan_amount = 275000
down_payment = 0.05*loan_amount
loan_term = 15 # in years
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


# Plot pie chart
plt.figure(1)
labels = ['Principal', 'Interest']
sizes = [loan_amount, int_total]
colors = ['#66b3ff', '#ff9999']
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
plt.axis('equal')
plt.title("Principal vs Interest Payments")
plt.savefig('pie_chart.png')

# Plot bar chart
plt.figure(2)
years = list(range(1, loan_term + 1))
principal_yearly = [sum(payment[1] for payment in payments[i*12:(i+1)*12]) for i in range(loan_term)]
interest_yearly = [sum(payment[2] for payment in payments[i*12:(i+1)*12]) for i in range(loan_term)]

bar_width = 0.35
ind = years

p1 = plt.bar(ind, principal_yearly, bar_width, color='#66b3ff', label='Principal')
p2 = plt.bar(ind, interest_yearly, bar_width, color='#ff9999', label='Interest', bottom=principal_yearly)

plt.ylabel('Amount ($)')
plt.xlabel('Years')
plt.title('Yearly Principal and Interest Payments')
plt.xticks(ind)
plt.legend((p1[0], p2[0]), ('Principal', 'Interest'))
plt.savefig('bar_chart.png')

# Show plots
plt.show()


