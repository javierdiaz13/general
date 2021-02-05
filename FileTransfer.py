'''
****************************************************
Title: File Transfer
Date: February 4th, 2020
Author: Javier Diaz
Purpose: To move files from the C drive to a flash
    drive so that mom could access the work she did 
    for the taxes.
****************************************************
'''

import shutil
import os

# Global Variables

# C Drive
cDrive='C:\\UTS20\\Users\\Guest'

# F Drive Old Computer
fDrive='F:\\UTS20\\Users\\Guest'

# E Drive New Computer
eDrive='E:\\UTS20\\Users\\Guest'


def workToHomeArriving():
    shutil.rmtree(cDrive)
    shutil.copytree(fDrive, cDrive)
    print("Files successfully copied from the Flash Drive to the Computer")

def workToHomeLeaving():
    shutil.rmtree(fDrive)
    shutil.copytree(cDrive, fDrive)
    print("Files successfully copied from the Computer to the Flash Drive")

def homeToWorkArriving():
    shutil.rmtree(cDrive)
    shutil.copytree(eDrive, cDrive)
    print("Files successfully copied from the Flash Drive to the Computer")

def homeToWorkLeaving():
    shutil.rmtree(eDrive)
    shutil.copytree(cDrive, eDrive)
    print("Files successfully copied from the Flash Drive to the Computer")

def main():
    ans = input('Are you leavin')
    if ans in ['H', 'Home', 'home']:
        homeToWork()
    elif ans in ['W', 'Work', 'work']:
        workToHome()
    else:
        