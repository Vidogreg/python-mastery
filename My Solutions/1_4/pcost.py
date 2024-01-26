def portfolio_cost(filename):
    portfolio_price = 0
    with open(filename, 'rb') as f:
        for line in f:
            try:
                portfolio_price += int(line.split()[1])*float(line.split()[2])
            except ValueError as e:
                print('Cannot parse: ' + str(line))
                print('Reason: ' + str(e))
    return portfolio_price

# print(portfolio_cost('Data/portfolio.dat'))
print(portfolio_cost('Data/portfolio3.dat'))