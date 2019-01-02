# https://www.business.qld.gov.au/running-business/finances-cash-flow/managing-money/break-even-point


def gross_profit():
    """Gross profit = sales revenue - costs of goods sold (cogs)"""
    sales_revenue = float(input("Expected sales revenue: "))
    cogs = float(input("Cost of goods sold: "))
    gross_profit = sales_revenue - cogs
    print("Sales Revenue: {}\nCOGS: {}\nGross Profit: {}".format(sales_revenue, cogs, gross_profit))
    return gross_profit, sales_revenue


def gross_profit_margin(gross_profit, sales_revenue):
    """Gross profit margin is the proportion of money left over from revenues after accounting for
    the cost of goods sold, and is found by dividing gross profit by revenues."""
    gross_profit_margin = (gross_profit / sales_revenue) * 100
    print("Gross profit margin: {}".format(gross_profit_margin))
    return gross_profit_margin


def break_even(gross_profit_margin):
    """The break-even analysis calculates the point where your business has reached a zero balance
    i.e. when your income covers your expenses exactly. """

    # Create a dictionary for user input
    fixed_costs = {}

    # Request information for the calculation of a break even point
    print("What are your fixed costs - i.e. salary, instruments, etc.")
    while True:
        try:
            item = input("Please enter expense name or done to compute results: ").capitalize()
            if item == 'Done':
                break
            else:
                cost = float(input("Cost $: "))
                fixed_costs[item] = cost
        except:
            print("Invalid value entered, please try again. ")


def contribution_margin():
    """"""
    variable_costs = {}
    # Request information for the calculation of a the contribution margin
    print("What are your vairable costs - i.e. printing, cover sleeves, etc.")
    while True:
        try:
            item = input("Please enter expense name or done to compute results: ").capitalize()
            if item == 'Done':
                break
            else:
                cost = float(input("Cost $: "))
                variable_costs[item] = cost
        except:
                print("Invalid value entered, please try again. ")
    sales_price = float(input("What price are you selling your goods for?"))
    total_variable_costs = sum(variable_costs.values())
    contribution_margin = sales_price - total_variable_costs

    print("Variable costs: {}\nTotal variable costs: {}\nContribution margin: {}".format(variable_costs, total_variable_costs, contribution_margin))
    return contribution_margin

def be_contribution_margin(cont_margin):
    """The break-even analysis calculates the point where your business has reached a zero balance
    i.e. when your income covers your expenses exactly. """

    # Create a dictionary for user input
    fixed_costs = {}

    # Request information for the calculation of a break even point
    print("What are your fixed costs - i.e. salary, instruments, etc.")
    while True:
        try:
            item = input("Please enter expense name or done to compute results: ").capitalize()
            if item == 'Done':
                break
            else:
                cost = float(input("Cost $: "))
                fixed_costs[item] = cost
        except:
            print("Invalid value entered, please try again. ")

    total_fixed_costs = sum(fixed_costs.values())
    contribution_margin = cont_margin
    break_even_point = total_fixed_costs / contribution_margin

    print("Fixed costs: {}\nTotal fixed costs: {}\nContribution margin: {}\nBreak even point in units: {}".format
          (fixed_costs, total_fixed_costs, contribution_margin, break_even_point))


# gross_profit, sales_revenue = gross_profit()
# gross_profit_margin(gross_profit, sales_revenue)

contribution = contribution_margin()
be_contribution_margin(contribution)
