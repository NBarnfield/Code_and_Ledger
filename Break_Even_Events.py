variable_costs = 0
fixed_costs = None

https://www.business.qld.gov.au/running-business/finances-cash-flow/managing-money/break-even-point

# Set While loop to ask the user for their fixed and variable costs

while True:
    try:
        variable = input("Please enter a float or integer that represents a variable cost, or done to continue.")
        if variable == 'done': break
        variable = float(int(variable))
        variable_costs = variable + variable_costs
    except ValueError:
        print("That is not a valid input. PLease enter a float, integer or the string 'done' to continue.")

while True:
    try:
        variable = input("Please enter a float or integer that represents a variable cost, or done to continue.")
        if variable == 'done': break
        variable = float(int(variable))
        variable_costs = variable + variable_costs
    except ValueError:
        print("That is not a valid input. PLease enter a float, integer or the string 'done' to continue.")

print('Variable costs total:', variable_costs)
print('Fixed costs total: ', fixed_costs)

input = ("What is your contribution margin?")

sale_price = input('What is the price of your tickets?')



print('As the break even point is ')




print(
