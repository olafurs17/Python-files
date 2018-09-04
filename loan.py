# Hofuðstóll lánsins lesin inn.
cost_str = input("Input the cost of the item in $: ")

# str breytu breytt í float breytu.
cost_float = float(cost_str) 

# if segð til að ákvarða vexti á láni.
if cost_float <= 1000:
    interest_monthly = 0.015
elif cost_float > 1000:
    interest_monthly = 0.02

# Föst greiðsla á mánuði.
pay_monthly = 50.0
month = 0
interest_total = 0

# While lykkja til að ákvarða hvenær lán er uppborgað.
while cost_float > 0:
    month += 1

# Vextir og eftir stöðvar reiknaðir.
    pay_interest = (interest_monthly * cost_float)
    cost_float = (cost_float + pay_interest) - pay_monthly
    interest_total += pay_interest 
    
# Heldarvextir settir í síðasta gjaldaga og gjaldagi settur í 0.
    if cost_float < 0:
       pay_monthly = interest_total
       cost_float = 0.0

# Prentað út á skjá upplýsingar um greiðslu lánsins.
    print('Month:', round(month), 'Payment:', round(pay_monthly, 2), 
          'Interest paid:', round(pay_interest, 2), 'Remaining debt:', round(cost_float,2))

# Auðri línu bætt við.
print('')

# Samantekt fjöldi mánaða og heildarvextir prentað út.
print('Number of months:', month)
print('Total interest paid:', round(interest_total, 2))
