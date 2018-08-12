import json
import GPSCalculator
import math

f = open('../customers.txt')

office = (math.radians(53.339428), math.radians(-6.257664))

for line in f:
    customer = json.loads(line)
    loc = (math.radians(float(customer['latitude'])), math.radians(float(customer['longitude'])))
    calc = GPSCalculator.GPSCalculator()
    print(calc.distance(loc, office))
