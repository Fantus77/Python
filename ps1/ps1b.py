def first(Annual_Salary, Portion_Saved, Total_Cost, Semi_Annual_Raise):
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
        if DivisibleBySix(Months):
            Annual_Salary = (Annual_Salary * Semi_Annual_Raise) + Annual_Salary
            Monthly_Salary = Annual_Salary / 12

    print("The total amount of months to save:", Months)

def DivisibleBySix(Months):
    floatVal = Months / 6.0
    wholeNum = int(floatVal)
    if (floatVal - wholeNum == 0):
        return True
    else:
        return False

def runme():
    Annual_Salary = int(input("Please enter annual salary:"))
    Portion_Saved = float(input("Please enter percentage of monthly salary to save:"))
    Total_Cost = int(input("Please enter the total cost of dream home:"))
    Semi_Annual_Raise = float(input("Please enter your annual raise percentage:"))
    first(Annual_Salary, Portion_Saved, Total_Cost, Semi_Annual_Raise)


runme()