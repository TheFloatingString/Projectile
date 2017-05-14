#!/usr/bin/env python

"""
THIS PROGRAM CALCULATES THE DISTANCE OF A PROJECTILE BASED ON ITS SPEED
AND ITS ANGLE RELATIVE TO THE GROUND
THIS PROGRAM IS COMPLETELY TEXT-BASED
MATH EQUATIONS WERE MADE AVAILABLE WITH THE HELP OF QUISHI WANG
PYTHON 3 SCRIPT PROGRAMMED BY LAURENCE LIANG
"""

# IMPORT MODULES
from math import *          # Import all methods/attributes from math module
import sys                  # Import sys.exit()

# DECLARE VARIABLES
theta = 0.0                 # theta = angle at which the projectile is launched
velocity = 0.0              # velocity = speed of the projectile
percent_distance_var = 0.0  # percent_distance_var = percentage of the covered distance
max_distance_var = 0.0      # max_distance_var = maximum distance
covered_distance_var = 0.0  # covered_distance_var = covered distance
g = 9.80665                 # g = gravitational constant
choice = 0                  # User's choice

# DEFINE FUNCTIONS

# Covered distance
def covered_distance(theta_, velocity_):   # Arguments: (theta, speed, covered_distance_var)
    theta_ = theta_*0.0174532925
    velocity= velocity_*0.0174532925
    covered_distance_var_ = (2/g)*((velocity_)**2)*sin(theta_)*cos(theta_) # Calculate 0.2041*((velocity)**2)*sin(theta)*cos(theta)
    return covered_distance_var_         # Return covered_distance_var

# Maximum distance
def max_distance(velocity):    # Arguments: (speed, max_distance_var)
    max_distance_var = (velocity**2)/g        # Calculate ((velocity)**2)/g
    return max_distance_var     # Return max_distance_var

# Percentage of maximum distance
def percent_distance(theta):  # Arguments: (theta, percent_distance_var)
    theta = theta*0.0174532925
    percent_distance_var = 100*(2*sin(theta)*cos(theta))  # Calculate 2*sin(theta)*cos(theta)
    return percent_distance_var                     # Return percent_distance_var

# Asks user
def ask_values():
    theta = float(input("Angle de la projectile (degrées): \t"))
    velocity = float(input("Vitesse de la projectile (m/s): \t"))
    return theta, velocity

def main():# Main method
    print("Ce logiciel permet de caluler des valeurs associées à la trajectoire d'une projectile \n \n")  # Display choices:
    print("Vous pouvez taper: \nLa touche 'T' \t\t pour calculer la trajectoire de la projectile")
    print("Tout autre touche \t pour quitter ce logiciel\n")

    while True:
        choice = input("\nChoix de l'usager: ") # Ask user for computation
        if choice.lower() != 't': # If not, sys.exit()
            sys.exit()
        else:
            theta, velocity = ask_values()
            covered_distance_var = covered_distance(theta, velocity)
            print("\nDistance parcourue de la projectile: \n{} \t mètres\n".format(covered_distance_var))
            max_distance_var = max_distance(velocity)
            print("Distance maximale avec cette vitesse: \n{} \t mètres\n".format(max_distance_var))
            percent_distance_var = percent_distance(theta)
            print("Pourcentage de la distance maximale avec cette inclinaison: \n{} %\n".format(percent_distance_var))

# EXECUTE CODE
if __name__ == "__main__":   # If "__main__" statement
    main()  # Main() method
