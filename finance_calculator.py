monthly_income = int(input("Enter your monthly income: "))
total_monthly_expenses = int(input("Enter your total monthly expenses: "))
monthly_savings = monthly_income - total_monthly_expenses
print(f"Your monthly savings are: ${monthly_savings}")
projected_annual_savings = (monthly_savings * 12 + (monthly_savings * 12 * 0.05))
print(f"Your projected annual savings are: ${projected_annual_savings}")