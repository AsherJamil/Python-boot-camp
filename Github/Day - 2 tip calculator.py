print("Welcome to the tip calculator")
bill = float(input("\nWhat was the total bill"))
tip = int(input("how much tip would you like to give 10,12 or 15"))
people = int(input("How many people will split the bill"))
tip_as_percent = tip/100
total_tip_amount = bill *tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
final_amount = round(bill_per_person,2)
print("your amount is=")
print(bill_per_person)