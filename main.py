# MaliTracker - FNB App Academy
# Languages: English, isiZulu, isiXhosa
# Author: qwarhakazindzingane-droid

print("MaliTracker - Daily Income & Savings")
print("Sawubona / Molo - Financial Inclusion")

def calculate_profit(income, expense):
    profit = income - expense
    family = profit * 0.7
    savings = profit * 0.3
    return profit, family, savings

# Example trader day
income = 1500  # Sales: amagwinya, chips, airtime
expense = 700  # Stock

profit, family, savings = calculate_profit(income, expense)

print(f"Income: R{income}")
print(f"Expense: R{expense}")
print(f"Profit: R{profit}")
print(f"Family Money: R{family}")
print(f"Savings: R{savings}")
print("Offline-first | Built for 6M SA informal traders")
