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
import pathlib
from pathlib import Path
import os

# Global Variables

# C Drive
cDrive='C:\\UTS20\\Users\\Guest'

# F Drive Old Computer
fDrive='F:\\UTS20\\Users\\Guest'

# E Drive New Computer
eDrive='E:\\UTS20\\Users\\Guest'

# Location of index.htm file in  Computer
indexFileC='C:\\UTS20\\TWHomepage\index.htm'

# Location of index.htm file in E Drive (New)
indexFileE='E:\\UTS20\\TWHomepage\index.htm'

# Location of index.htm file in F Drive (Old)
indexFileF='F:\\UTS20\\TWHomepage\index.htm'

def createBackup(drive):
    name=str(input('Give the name of the Backup Folder you want to create: '))
    backupFileLoc='C:\\{}'.format(name)
    while pathlib.Path(backupFileLoc).exists():
        print('The backup folder already exist. Pick a new name or delete the existing folder\n')
        name=input('Give the name of the Backup Folder you want to create: ')
    #os.mkdir(backupFileLoc)
    shutil.copytree(drive, backupFileLoc)

def homeToWorkLeaving():
    shutil.rmtree(eDrive)
    os.remove(indexFileE)
    shutil.copy(indexFileC, indexFileE)
    shutil.copytree(cDrive, eDrive)
    print("Files successfully copied from the Flash Drive to the Computer\n")

def homeToWorkArriving():
    shutil.rmtree(cDrive)
    os.remove(indexFileC)
    shutil.copy(indexFileF, indexFileC)
    shutil.copytree(fDrive, cDrive)
    print("Files successfully copied from the Flash Drive to the Computer\n")

def workToHomeLeaving():
    shutil.rmtree(fDrive)
    os.remove(indexFileF)
    shutil.copy(indexFileC, indexFileF)
    shutil.copytree(cDrive, fDrive)
    print("Files successfully copied from the Computer to the Flash Drive\n")

def workToHomeArriving():
    shutil.rmtree(cDrive)
    os.remove(indexFileC)
    shutil.copy(indexFileE, indexFileC)
    shutil.copytree(eDrive, cDrive)
    print("Files successfully copied from the Flash Drive to the Computer\n")

# Kid Proofing
leave_arrive = input('Are you leaving or arriving?\n')
# If something was typed incorrectly than you will be prompted again to choose a correct
# leave or arrive option
while leave_arrive not in ['Leave', 'leave', 'l', 'L', 'Leaving', 'leaving', 'Arrive', 'arrive', 'a', 'A', 'arriving', 'Arriving']:
    print('You must have spelled something wrong. Try Again\n')
    leave_arrive = input('Are you leaving or arriving?\n')

if leave_arrive in ['Leave', 'leave', 'l', 'L', 'Leaving', 'leaving']:
    # Leaving
    createBackup(cDrive)
    home_work = input('Home or Work?\n')
    if home_work in ['Home','home', 'H']:
        # Leaving the house, going to hackensack
        homeToWorkLeaving()
    else:
        workToHomeLeaving()
else:
    # Arriving
    home_work = input('Home or Work?\n')
    if home_work in ['Home','home', 'H']:
        # Left work, arriving at home
        workToHomeArriving()
    else:
        # Left home, arriving in hackensack
        homeToWorkArriving()
exit()