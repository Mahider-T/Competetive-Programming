# Enter your code here. Read input from STDIN. Print output to STDOUT
from math import atan,degrees
AB=int(input())
BC=int(input())
print(str(round(degrees(atan(AB/BC))))+"\u00b0")