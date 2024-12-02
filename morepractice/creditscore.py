def hasCreditScore(age):
    if(age >=18 and age <=70):
        return True
    return False

def hasIncome(annual_income,monthly_income):
    if(annual_income >= 50000 or monthly_income >= 3000):
        return True
    
    return False

def hasLoanDefault(defaultStatus):
    if defaultStatus:
        return True
    
    return False

def main():
    age = int(input('Enter your age \n'))

    monthly_income = float(input('Enter your monthly income \n'))
    annual_income = float(input('Enter your annual income \n'))
    hasDefault = bool(input('Have you had any Loans defaulted? Press 1 for Yes, 0 for No: \n'))

    if not (hasLoanDefault(hasDefault)) and hasIncome(annual_income,monthly_income) and hasCreditScore(age):
        print('You qualify for a Loan')
    else:
        print('You do NOT qualify for any limit')

main()


