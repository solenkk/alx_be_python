#!/usr/bin/env python3
# finance_calculator.py

# Prompt the user for financial details
monthly_income = float(input("Enter your monthly income: "))
monthly_expenses = float(input("Enter your total monthly expenses: "))

# Calculate monthly savings
monthly_savings = monthly_income - monthly_expenses

# Calculate projected annual savings with 5% interest
annual_savings_without_interest = monthly_savings * 12
interest_earned = annual_savings_without_interest * 0.05
projected_annual_savings = annual_savings_without_interest + interest_earned

# Display the results
print(f"Your monthly savings are ${monthly_savings:.0f}.")
print(f"Projected savings after one year, with interest, is: ${projected_annual_savings:.0f}.")
