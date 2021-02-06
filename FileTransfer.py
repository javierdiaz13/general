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

# Global Variables

# C Drive
cDrive='C:\\UTS20\\Users\\Guest'

# F Drive Old Computer
fDrive='F:\\UTS20\\Users\\Guest'

# Location of index.htm file in Old Computer
fIndex='C:\UTS20\TWHomepage'

# E Drive New Computer
eDrive='E:\\UTS20\\Users\\Guest'

def createBackup(drive):
    name=input('Give the backup folder a name')
    shutil.copytree(drive, 'C:\\{}'.format(name))

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


leave_arrive = input('Are you leaving or arriving?')
if leave_arrive in ['Leave', 'leave', 'l', 'L', 'Leaving', 'leaving']:
    ans1 = input('Home or Work?')
    if ans1 in ['Home','home', 'H']:
        homeToWorkLeaving()
    else:
        workToHomeLeaving()
else:
    if ans1 in ['Home','home', 'H']:
        homeToWorkArriving()
    else:
        workToHomeArriving()
exit()