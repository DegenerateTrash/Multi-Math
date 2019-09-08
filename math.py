from math import *

import values

def main():
    choice = int(input("Choice: "))
    if choice == 1:
        cirarea()
    elif choice == 2:
        circum()
    elif choice == 3:
        pyth()
    return

def cirarea():
    rad = float(input("Radius: "))
    print("The area is {0:.100f}".format(float(values.pi)* pow(rad, 2) ))
def circum():
    diam = float(input("Diameter: "))
    print("The circumference is {0:.41f}".format(float(values.pi)* diam ))
def pyth():
    sidewant = str(input("Side: "))       #  |\
    if sidewant.lower() == "c":           # a|_\ c
        a = float(input("Side a"))        #   b
        b = float(input("Side b"))
        print("Side C = {0:0.41f}".format( sqrt(pow(a,2) + pow(b,2) )))
main()