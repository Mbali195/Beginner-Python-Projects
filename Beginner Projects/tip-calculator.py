print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12 or 15? "))
tip_convert = tip / 100
people = int(input("How many people to split the bill? "))
tip_calculator = (bill * tip_convert) 
total_each = (tip_calculator + bill) / people
final_amount = round(total_each, 2) 
#the rounding up works well but in order to show a zero at the end best to round it up like this: (found on stack overflow)
final_amount = "{:.2f}".format(total_each)

print(f"Each person should pay ${final_amount}")