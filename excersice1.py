monthlySalary = int(input("Enter your monthly salary: "))

monthName = input("Enter the name of the month: ")

savings = (int(input("Enter the percentage you want to save: "))*monthlySalary)/100
 
rent = (int(input("Enter the percentage you pay for rent: "))*monthlySalary)/100

electricity = (int(input("Enter the percentage you pay for electricity: "))*monthlySalary)/100

total = savings + rent + electricity

def expenses():
    print("Your Savings are: ", savings)
    print("Your Rent is: ", rent)
    print("Your Electricity is: ", electricity)

def totalExpenses():
    totalExpenses = savings + rent + electricity
    print("Your total expenses are: ", totalExpenses)

def Remaining():
    remaining = monthlySalary - total
    print("Your remaining salary is: ", remaining)

def yearlyRentElectricity():
    yearlyRent = rent * 12
    yearlyElectricity = electricity * 12
    yearlyTotal = yearlyRent + yearlyElectricity
    print("Your yearly total expenses are: ", yearlyTotal)

def justForFun():
    monthlyFun = monthlySalary ** 12
    print("MonthlySalary powered by 12 ", monthlyFun)

expenses()
totalExpenses()
Remaining()
yearlyRentElectricity()
justForFun()