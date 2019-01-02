# https://www.business.qld.gov.au/running-business/finances-cash-flow/managing-money/break-even-point

#
# def gross_profit():
#     """Gross profit = sales revenue - costs of goods sold (cogs)"""
#     sales_revenue = float(input("Expected sales revenue: "))
#     cogs = float(input("Cost of goods sold: "))
#     gross_profit = sales_revenue - cogs
#     print("Sales Revenue: {}\nCOGS: {}\nGross Profit: {}".format(sales_revenue, cogs, gross_profit))
#     return gross_profit, sales_revenue
#
#
# def gross_profit_margin(gross_profit, sales_revenue):
#     """Gross profit margin is the proportion of money left over from revenues after accounting for
#     the cost of goods sold, and is found by dividing gross profit by revenues."""
#     gross_profit_margin = (gross_profit / sales_revenue) * 100
#     print("Gross profit margin: {}".format(gross_profit_margin))
#     return gross_profit_margin


def break_even(gross_profit_margin):
    # Create a dictionary for user input
    fixed_costs = {}
    # Request information for the calculation of a break even point
    print("What are your fixed costs - i.e. salary, instruments, etc.")
    while True:
        try:
            item = input("Please enter expense name or Done to compute results: ").capitalize()
            if item == 'Done':
                break
            else:
                cost = float(input("Please enter a float or integer that represents a variable cost, or done to continue."))
                fixed_costs[item] = cost
        except:
            print("Invalid value entered, please try again. ")

    for x, y in fixed_costs:
        print(x, y)

    # Summarise values
    total_costs = sum(fixed_costs.values())

    while True:
        try:
            gross_profit_margin = float(input("What profit margin do you expect to make- i.e. 10% = .10?"))
            break
        except:
            print("Invalid value entered, please try again. ")

    break_even_point = total_costs / gross_profit_margin

    print("Your total costs are {}, and you anticipate a gross profit margin of {}. "
          "To achieve this your break even point it {}.".format(total_costs, gross_profit_margin, break_even_point))

gross_profit, sales_revenue = gross_profit()
gross_profit_margin(gross_profit, sales_revenue)


# break_even()
#
# print("When determining the pricing of products you can choose between two different approaches. Each returns the same"
#       "result however approaches it from a different angle. The break even point lets you know how much of a product"
#       "you need to sell before you begin to make profit. The contribution margin indicates what percentage of a "
#       "product's sale price goes towards an end profit goal. The difference is whether you have an end profit goal or "
#       "not.")
#
# option = input("Are you interested in working out the break even point (units of product required to be sold to break "
#                "even) or to find out the contribution margin of your products (how much profit you get from each "
#                "sale)?")
#
# while True:
#     if option == "contribution margin":
#         contribution_margin()
#     elif option == "break even":
#         break_even()
#     elif option == "done":
#         break
#     else:
#         print("Invalid option. Please enter contribution margin, break even, or done to exit.")
