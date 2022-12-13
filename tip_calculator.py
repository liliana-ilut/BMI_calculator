#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print ("Welcome to the tip calculator program")
bill = float(input("What was the total bill? $"))
tip = int(input("What is the percentage tip you would like to give 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))

# print(type(bill))
individual_pay = (bill + tip/100 * bill)/people

#round the final number to 2 decimals
# final_amount = round(individual_pay,2)
final_amount = "{:.2f}".format(individual_pay)

#print how much each person will pay
print(f"Each person should pay ${final_amount}")