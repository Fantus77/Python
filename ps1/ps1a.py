"""
Annual_Salary - Input by user: How much money they make in a year
Portion_Saved - Input by user: How much of their salary per month they will put in savings (needs to be decimal)
Total_Cost - Input by user: How much the home costs
Portion_Down_Payment - How much of the Total_Cost needs to be in savings (25%)
Current_Savings - The amount that has been collected that needs to == Down_Payment_Amount (Starts at 0)
r - This is the annual return on investment from Current_Savings (4%)
Monthly_Salary - This needs to be figured out from Annual_Salary to determine salary on monthly basis (Annual_Salary / 12)
Put_Away - How much money should be added to Current_Savings each month (Monthly_Salary * Portion_Saved)
Down_Payment_Amount - This is the amount that needs to be == Current_Savings
"""

"""
# Need to take the value entered for Annual_Salary, Portion_Saved, and Total_Cost
# Annual_Salary = input()
# Portion_Saved = input()
# Total_Cost = input()


# Down_Payment_Amount
Total_Cost * Portion_Down_Payment

# Current_Savings
Current_Savings = 0

# r
r = 0.04

# Monthly_Salary
Monthly_Salary = Annual_Salary / 12

# Put_Away
(Monthly_Salary * Portion_Saved) + (Current_Savings * r / 12)
"""
# Let's do this where we work in a chain. Starting with collecting the inputs and then moving to the next function where they are calculated and passed to the next function which does the next calculation

def first(Annual_Salary, Portion_Saved, Total_Cost):
# setting up what the monthly salary is as well as how much the down payment should be and the ROI percentage
    Monthly_Salary = Annual_Salary / 12
    Portion_Down_Payment = 0.25
    r = 0.04
# figuring out how much the down payment should be based on the total cost
    Down_Payment_Amount = Total_Cost * Portion_Down_Payment
    Down_Payment_Amount = int(Down_Payment_Amount)
# adding to Current_Savings until it is >= Down_Payment_Amount
    Current_Savings = 0
    Months = 0
    while Current_Savings <= Down_Payment_Amount:
        Current_Savings = Current_Savings + ((Monthly_Salary * Portion_Saved) + (Current_Savings * r / 12))
        Months = Months + 1
        # print(Current_Savings)
    print("The total amount of months to save:", Months)
        # Current_Savings = int(Current_Savings)
# # once Current_Savings == Down_Payment_Amount dividing Down_Payment_Amount by how much Current_Savings is increased by each month to figure out how many months it will take to save up the amount needed. Then trying to print that out
#     if Current_Savings >= Down_Payment_Amount:
#         Months = Down_Payment_Amount / ((Monthly_Salary * Portion_Saved) + (Current_Savings * r / 12))
#         Months = int(Months)
#         print(Months)

# first(120000, 0.10, 1000000)
# first(80000, 0.15, 500000)


def runme():
    Annual_Salary = int(input("Please enter annual salary:"))
    Portion_Saved = float(input("Please enter percentage of monthly salary to save:"))
    Total_Cost = int(input("Please enter the total cost of dream home:"))
    # print(Annual_Salary)
    first(Annual_Salary, Portion_Saved, Total_Cost)


runme()