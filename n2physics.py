#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# This is a basic calculator script to detect the total net force of an object using mass and
# acceleration following the equation "F = ma" for Newton's 2nd law in classical mechanics. 
#
# Version 1.2
# Script will be updated periodically for better accessibility and usability of calculator.
"""
Created on Mon Sep  2 17:50:37 2019
@author: TheRun98
"""
import time

while True:
    accel = input("Enter acceleration of object in m/s\N{SUPERSCRIPT TWO}: ")
    accel_value = float(accel)
    if accel_value <= -0.00000000001:
        yes_no = input("You have put in a value of deceleration. Continue? ")
        if yes_no == "no" or yes_no == "No":
            print("User selected '" + yes_no + "'. Please try again.\n")
            continue
        else:
            print("Storing data...")
            break
        continue            
    else:
        print("Storing data...")
        break
    continue
    
while True:
    mass = input("Enter mass of object in kilograms: ")
    mass_value = float(mass)
    if mass_value <= 0:
        print("Mass cannot be 0 kg or lower. Please input a positive value.\n")
        continue
    else:
        print("Calculating total net force...\n")
        time.sleep(0.5)
        break
    
object_force = str(round(accel_value * mass_value, 3))
print("The total net force of the object is " + object_force + " N.")
