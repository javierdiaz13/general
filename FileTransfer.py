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

# F Drive
fDrive='F:\\UTS20\\Users\\Guest'

# E Drive
eDrive='E:\\UTS20\\Users\\Guest'


def workToHome(src,dst):
    shutil.copytree(cDrive, fDrive)
    print("Files successfully copied from the Computer to the Flash Drive")


def homeToWork(src,dst):
    shutil.copytree(eDrive, cDrive)
    print("Files successfully copied from the Flash Drive to the Computer")

