'''
--#annual_interest_rate = 0.0
--#monthly_interest_rate = annual_interest_rate
--#monthly_payment = monthly_payment_rate * balance
--#new_balance= (balance - monthly_payment) * (1 + monthly_interest_rate)
--#print('Month: %d  Minimum monthly payment: %g  Remaining balance: %g'\
--  #% (month, round(monthly_payment, 2), round(balance,2)))

Input the cost of the item in $: 500
Month: 1 Payment: 50.0 Interest paid: 7.5 Remaining debt: 457.5
Month: 2 Payment: 50.0 Interest paid: 6.86 Remaining debt: 414.36
'''
cost = 500
interest_monthly =0.015
pay_monthly = 50.0
for month in range(1, 13):
    pay_interest = interest_monthly * cost
    cost = ((cost + pay_interest)  - pay_monthly)
    print('month', round(month), 'Payment: ', round(pay_monthly, 2), 'Interest paid: ', round(pay_interest, 2), 'Remaining dept: ', round(cost,2))
   