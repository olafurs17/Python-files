'''num_ask_str = input("Sláið inn tölu frá 1 til 86400: ")
num_tala = int(num_ask_str)
print("Klukkutímar:", round((num_tala / 60) / 60, 1))
print("Mínótur:", round(num_tala / 60, 1))
print(num_tala, "Sekúndur eru", round(num_tala /60), "Mínótur og", round((num_tala / 60) / 60, 1), "Klukkutímar")
'''

secs_str = input("Input seconds: ") # do not change this line
secs_int = int(secs_str)
hours = round((secs_int / 60) / 60, 1)
minutes = round(secs_int / 60, 1)
seconds = round(secs_int / 60)
print(hours,":",minutes,":",seconds) # do not change this line
