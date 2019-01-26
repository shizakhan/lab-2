print('shiza khan','18b-130-cs(a)')
print('lab 2','programming ex 2')
print('\n')
import math
length = eval(input('enter the length: '))
degree = eval(input('enter the angle: '))
#converting degree into radians
angle = (math.pi*degree)/180
#computing height
height = length*math.sin(angle)
print(height)
