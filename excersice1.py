list1 = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

month = int(input("Enter the month in numbers (from 1 to 12): "))

monthlySalary = float(input(f"Your salary for {list1[month - 1]} is:"))

savings = (float(input("Enter the percentage you want to save: "))*monthlySalary)/100
 
rent = (float(input("Enter the percentage you pay for rent: "))*monthlySalary)/100

electricity = (float(input("Enter the percentage you pay for electricity: "))*monthlySalary)/100

total = savings + rent + electricity

def expenses(s, r, e):

    print("Your Savings are: ", s)
    print("Your Rent is: ", r)
    print("Your Electricity is: ", e)

def totalExpenses(s, r, e):

    totalExpenses = s + r + e
    print("Your total expenses are: ", totalExpenses)

def Remaining(ms, t):

    remaining = ms - t
    print("Your remaining salary is: ", remaining)

def yearlyRentElectricity(r, e):

    yearlyRent = r * 12
    yearlyElectricity = e * 12
    yearlyTotal = yearlyRent + yearlyElectricity
    print("Your yearly total expenses are: ", yearlyTotal)

def justForFun(ms):
    
    monthlyFun = ms ** 12
    print("MonthlySalary powered by 12 ", monthlyFun)

expenses(savings, rent, electricity)
totalExpenses(savings, rent, electricity)
Remaining(monthlySalary, total)
yearlyRentElectricity(rent, electricity)
justForFun(monthlySalary)