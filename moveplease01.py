#!/usr/bin/env python3

import shutil
import os

# import libraries
os.chdir('/home/student/mycode/')
shutil.move('raynor.obj', 'ceph_storage/')

def main():
    """called at runtime"""
    os.chdir('/home/student/mycode/') # move into the working directory
    shutil.move('raynor.obj', 'ceph_storage/') # try moving the file raynor.obj into the ceph_storage dir

    # program will pause while we accept input
    xname = input('What is the new name for kerrigan.obj? ') # collect string input from the user
    shutil.move('ceph_storage/kerrigan.obj', 'ceph_storage/' + xname) # moving kerrigan.obj into ceph storage with new name

if __name__ == "__main__":
    main()
