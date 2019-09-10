#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# This is a calculator script to detect the total net force of an object using mass and acceleration
# following the equation "F = ma" for Newton's 2nd law in classical mechanics. 
"""
Created on Mon Sep  2 17:50:37 2019

@author: TheRun98
"""
import sys

accel = input("Enter acceleration of object in m/s\N{SUPERSCRIPT TWO}: ")
accel_int = int(accel)
if accel_int <= -1:
    print("Acceleration cannot be a negative increment. Aborting program...")
    sys.exit()
else:
    print("Storing data...")
mass = input("Enter mass of object in kilograms: ")
mass_int = int(mass)
if mass_int <= 0:
    print("Mass cannot be 0 kg or lower. Aborting program...")
    sys.exit()
else:
    print("Thank you. Proceeding to calculating...")
    
object_force = accel_int * mass_int
ob_j = str(object_force)

print("The total net force of the object is " + ob_j + " N.")
