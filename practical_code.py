# loop control
for i in range(10):
    print(i)

for i in range(10):
    if(i == 6):
        break
    print(i)

for i in range(10):
    if(i == 6):
        continue
    print(i)



# formatted printing
name = 'Fero'
shares = 23
price = 1.234
print(f'{name:>10s} {shares:>10d} {price:>10.2f}')
print('{:10s} {:10d} {:10.2f}'.format(name,shares,price))
print('%10s %10d %10.2f' % (name, shares, price))



# no-op placeholder statement
pass



# 