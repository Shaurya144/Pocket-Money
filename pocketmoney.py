# First get user input on weekly allowance.
pocket_money = float(input("How much pocket money are you given per week? "))

# We also need to make sure it is a rational number.
pocket_money = round(pocket_money * 100)
pocket_money = pocket_money / 100

# Now we need to work out what they are left with once they spend some money.
weekly_spend = int(input("How much do you spend in a year"))
weekly_spend = round(weekly_spend * 100)
weekly_spend = weekly_spend / 100

overall_income = pocket_money - weekly_spend
yearly_income = overall_income * 52
print("Your annual income comes up to around " + str(yearly_income))
