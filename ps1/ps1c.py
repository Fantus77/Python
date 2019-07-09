
def first(Annual_Salary, Total_Cost, Semi_Annual_Raise, Total_Months):
# setting up what the monthly salary is as well as how much the down payment should be and the ROI percentage
    Monthly_Salary = float(Annual_Salary / 12)
    Portion_Down_Payment = 0.25
    Return_On_Investment = 0.04
# figuring out how much the down payment should be based on the total cost
    Down_Payment_Amount = Total_Cost * Portion_Down_Payment
# adding to Current_Savings until it is >= Down_Payment_Amount
    Current_Savings = 0.0
    Portion_Saved = 0.00
    while Current_Savings < Down_Payment_Amount:
        Months = 0
        Portion_Saved = Portion_Saved + 0.001
        Current_Savings = 0
        while Months < Total_Months:
            Current_Savings = float(Current_Savings) + float((Monthly_Salary * Portion_Saved) + (Current_Savings * Return_On_Investment / 12.0))
            Months = Months + 1
            if DivisibleBySix(Months):
                Annual_Salary = (Annual_Salary * Semi_Annual_Raise) + Annual_Salary
                Monthly_Salary = float(Annual_Salary / 12)
                
        if NearlyEqual(Down_Payment_Amount, Current_Savings, 100):
            print("You did it!")
        else:
            print("Not quite")

def DivisibleBySix(Months):
    floatVal = Months / 6.0
    wholeNum = int(floatVal)
    if floatVal - wholeNum == 0:
        return True
    else:
        return False

def NearlyEqual(target, current, tolerance):
    if current >= (target - tolerance) and current <= (target + tolerance):
        return True
    else:
        return False

def RateFinder():
    

# print(NearlyEqual(target, current, tolerance))
# test1 = NearlyEqual(-1, 3, 2)
# print(test1)



# second(Annual_Salary, 1000000, 0.07, Months)

def runme():
    # print("Test Case 1")
    # print(">>>")
    # print("Enter the starting salary: 150000")
    # print("Best savings rate: 0.4411")
    # print("Steps in bisection search: 12")
    # print(">>>")
    # print("Test Case 2")
    # print(">>>")
    # print("Enter the starting salary: 300000")
    # print("Best savings rate: 0.2206")
    # print("Steps in bisection search: 9")
    # print(">>>")
    # print("Test Case 3")
    # print(">>>")
    # print("Enter the starting salary: 10000")
    # print("It is not possible to pay the down payment in three years.")
    # print(">>>")
    Annual_Salary = int(input("Please enter the starting salary:"))
    # Portion_Saved = float(input("Please enter percentage of monthly salary to save:"))
    # Total_Cost = int(input("Please enter the total cost of dream home:"))
    # Semi_Annual_Raise = float(input("Please enter your annual raise percentage:"))
    # Months = 36
    # first(Annual_Salary, 1000000, 0.07, Months)
    first(Annual_Salary, 1000000, 0.07, 36)



runme()










# Unnecessary crap goes below here


"""
def second(Annual_Salary, Total_Cost, Semi_Annual_Raise, Months):
    Monthly_Salary = Annual_Salary / 12
    Portion_Down_Payment = 0.25
    Return_On_Investment = 0.04
    Down_Payment_Amount = Total_Cost * Portion_Down_Payment
    Required_Per_Month = Down_Payment_Amount / Months
    Percent_Of_Monthly_Salary = Required_Per_Month / Monthly_Salary
    # while Current_Savings <= Down_Payment_Amount:
    #     Current_Savings = Current_Savings + (Monthly_Salary)
    print("Here is the percentage of your monthly salary to save:", Percent_Of_Monthly_Salary)
"""