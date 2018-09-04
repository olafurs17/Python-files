#cost = int(input("Amount of money: "))
cost = 500
month_payment = 50.0
annual_interest_rate = 0.015

for month in range(1, 13):
    intrest_paid = cost * annual_interest_rate
    remain = (cost - month_payment) + intrest_paid 
    print("Month: ", (month), "Payment: ", round(month_payment, 2), "Intrest paid: ", round(intrest_paid, 2), "Remaining dept: ", round(remain, 2))
    
'''
monthly_payment = monthly_payment_rate * balance
    balance = (balance - monthly_payment) * (1 + monthly_interest_rate)
--month_payment_rate = 50.0
--#monthly_payment = float(monthly_payment)
--new_balance= (cost - month_payment) * (1 + month_interest_rate)
--#monthly_payment = monthly_payment_rate * balance
--#print('Month: %d  Minimum monthly payment: %g  Remaining balance: %g'\
--    #      % (month, round(monthly_payment, 2), round(balance,2)))
Input the cost of the item in $: 500
Month: 1 Payment: 50.0 Interest paid: 7.5 Remaining debt: 457.5
Month: 2 Payment: 50.0 Interest paid: 6.86 Remaining debt: 414.36
'''