#Calculator Shape
#import library
import math

#Area of a square
length_square= float(input('What is the length of a side of the square? '))
area_square = length_square*length_square
print('The area of the square is: '+ str(area_square))
print('\n')

#Area of a rectangle
lenght_rectangle=float(input('What is the length of rectangle? '))
width_rectangle=float(input('What is the width of the rectangle? '))
area_rectangle= float(lenght_rectangle*width_rectangle)
print('The area of the rectangle is ' + str(area_rectangle))
print('\n')

#Area of circle
radius_circle = float(input('What is the radius of the circle? '))
#strech 1 using the functio math.pi
area_circle = float((radius_circle**2)*math.pi)
print('The area of the circle is: ' + str(round(area_circle,2)))
print('\n')

#strech 2 to ask a new value for to do new calculate
new_length_value=float(input('What a new length value? '))
area_square = new_length_value*new_length_value
area_circle = float((new_length_value**2)*math.pi)
cube_circle = float ((new_length_value**3))
volume_sphere= round(float((4/3)*math.pi*(new_length_value**3)))
print('The area of the square is: '+ str(area_square))
print('The area of the circle is: ' + str(round(area_circle,2)))
print('The volume of cube is: ' + str(cube_circle))
print('The volume of sphere is: ' + str(volume_sphere))
print('\n')

#strech 3 displayng values in centimeter or meters

#area of square in centimeters and meters with conversion
length_square_cm=(float(input('What is the length of a side of the square (in cm)? ')))
area_square_cm=float(length_square_cm*2)
print('The area of the square is '+ str(area_square_cm)+'cm²')
print('The area of the square is '+ str(float(area_square_cm/10000))+'m²')
print('\n')

#area of rectangle in centimenters and meters with conversion
length_rectangle_cm=float(input('What is the length of rectangle in cm?'))
width_rectangle_cm=float(input('What is the width of rectangle in cm? '))
area_rectangle_cm = float(length_rectangle_cm*width_rectangle_cm)
print('The area of rectangle is '+ str(area_rectangle_cm)+'cm² (centimeters)')
print('The area of rectangle is '+ str(float(area_rectangle_cm/10000))+'m²(meters)')
print('\n')

#area of a circle
radius_circle_cm =float (input('What is the radius of the circle in cm? '))
area_circle_cm = float(round((radius_circle_cm**2)*math.pi))
print('The area of the circle is: ' + str(area_circle_cm)+ 'cm2 (centimeters)')
area_circle_m = round(area_circle/10000,6)
print('The area of the circle is: ' + str(area_circle_m)+ 'm2 (meters)')