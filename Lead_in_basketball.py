#1. Stigafjöldi liðs sem er leiðir leikin
points_str = input("Enter the lead in points: ")
points_remaining_int = int(points_str)

#2. Draga 3 stig frá
lead_calculation_float = float(points_remaining_int - 3)

#3. Bæta við 1/2 stigi ef liðið sem leiðir leikinn er með boltann.
#   og draga frá 1/2 stig ef hitt liðið er með boltann.
has_ball_str = input("Does the lead team have the ball (Yes or No): ")

if has_ball_str == 'Yes':
    lead_calculation_float = lead_calculation_float + 0.54
else:
    lead_calculation_float = lead_calculation_float - 0.5

#   Ef stig eru minni en núll þá verða þau núll.
if lead_calculation_float < 0:
    lead_calculation_float = 0

#4. Squera þetta með veldi í 2
lead_calculation_float = lead_calculation_float ** 2

#5. Ef útkomma er stærri en númer hjá þeim sem eru að tapa
#   þá er sigurinn ekki í hættu
seconds_remaining_int = int(input("Enter the number of the seconds remaining: " ))

if lead_calculation_float > seconds_remaining_int:
    print("Lead is safe.")
else:
    print("Lead is not safe.")
