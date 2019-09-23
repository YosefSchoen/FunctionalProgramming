
#  Example program for Targil 1
import math

# Area calculation program  
def rectangleArea(w, h):
     return w*h

def circleArea(r):
     return math.pi * r**2

def sphereVolume(r):
    return (4.0 / 3) * math.pi * r**3

def coneVolume(r, h):
    return (h * 3) * circleArea(r)

def pyramidVolume(l, w, h):
    return rectangleArea(l, w) * (h / 3)

def torus(r, R):
    return circleArea(r) * 2 * math.pi * R

# printing the menu options
def prtMenu(shapes):
   for i in range(len(shapes)):
      print (i+1, shapes[i])
   return

# main program

print ("Welcome to the Area calculation program")
print ("---------------------------------------\n")

# Print out the menu
shapes = ("Rectangle", "Circle", "Sphere", "Cone", "Pyramid", "Torus")

while True:
    print ("\nPlease select a shape (press 0 to quit):")
    prtMenu(shapes)

    # Get the user's choice: 
    shape = input("> ")

    # Calculate the area: 
    if shape == "1":
         height = float(input("Please enter the height: "))
         width  = float(input("Please enter the width: "))
         area = rectangleArea(width, height)
         print ("The area is", area)
         continue

    elif shape == "2":
         radius = float(input("Please enter the radius: "))
         area   = circleArea(radius)
         print ("The area is", area)
         continue

    elif shape == "3":
        radius = float(input("Please enter the radius: "))
        volume = sphereVolume(radius)
        print("The volume is", volume)
        continue

    elif shape == "4":
        radius = float(input("Please enter the radius: "))
        height = float(input("Please enter the height: "))
        volume = coneVolume(radius, height)
        print("The volume is", volume)
        continue

    elif shape == "5":
        length = float(input("Please enter the length: "))
        width = float(input("Please enter the width: "))
        height = float(input("Please enter the height: "))
        volume = pyramidVolume(length, width, height)
        print("The volume is", volume)
        continue

    elif shape == "6":
        minorRadius = float(input("Please enter the minorRadius: "))
        majorRadius = float(input("Please enter the majorRadius: "))
        volume = torus(minorRadius, majorRadius)
        print("The volume is", volume)
        continue

    elif shape == "0":
         print ("Bye!")
         break
    else:     
         print ("Invalid shape")
