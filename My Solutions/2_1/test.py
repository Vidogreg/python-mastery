# a
f = open('Data/ctabus.csv')
next(f)



# b
import tracemalloc
f = open('Data/ctabus.csv')
tracemalloc.start()
# data = f.read()
data = f.readlines()
len(data)
current, peak = tracemalloc.get_traced_memory()
print(current, peak)



# d
    # python 'My Solutions\2_1\readrides.py'

    # read_rides_as_tuples
    # Memory Use: Current 128,447,574, Peak 128,481,833

    # read_rides_as_dictionary
    # Memory Use: Current 220,856,422, Peak 220,890,681

    # read_rides_as_class
    # Memory Use: Current 179,274,990, Peak 179,309,249

    # read_rides_as_named_tuple
    # Memory Use: Current 133,073,272, Peak 133,107,531

    # read_rides_as_class_with_slots
    # Memory Use: Current 123,829,542, Peak 123,863,801