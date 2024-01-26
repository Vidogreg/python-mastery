portfolio_price = 0
with open('Data/portfolio.dat', 'rb') as f:
    for line in f:
        portfolio_price += int(line.split()[1])*float(line.split()[2])
print(portfolio_price)