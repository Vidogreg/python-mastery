import sys

sys.path.append('C:\\Users\\viktor.gregor\\_SUPERSCALE\\GitHub\\python-mastery\\My Solutions\\1_4')
import pcost
pcost.portfolio_cost('Data/portfolio2.dat')

sys.path.append('C:\\Users\\viktor.gregor\\_SUPERSCALE\\GitHub\\python-mastery\\My Solutions\\1_5')
from stock import Stock
s = Stock('GOOG', 100, 490.10)
s.name
s.cost()