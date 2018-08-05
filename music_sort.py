#!/usr/bin/env python

import os, sys, unicodedata, shutil     # native utilities
import eyed3    # audio file ID3 package

def main():
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')
    print('~~~~~~~~~~~~~~~~~~  MUSIC SORTER  ~~~~~~~~~~~~~~~\n')
    print('~~~~~~~~~~~  Northwestern University  ~~~~~~~~~~~\n')
    path_root = str(raw_input('Please enter destination folder:'))
    # Setup detection/expansion of '~' home shortcut
    # path cleanup:
    if os.getcwd() != '/':
        print("Changing working directory to '/'...\n")
        os.chdir('/')
    if path_root.find('~') != -1: # Expand ~ to /home/<user>
        path_root = os.path.expanduser(path_root)
    if path_root[-1] != '/': # Append missing slash
        path_root += '/'
    if not os.path.exists(path_root): # Check for existance
        print('ERROR: The path you input could not be found\n')
        print('Exiting...')
        # return
    print('Creating destination folder at ' + path_root + '_sorted')
    os.makedirs(path_root + '_sorted')
    print('Begning sort...')
    sift(path_root)

def sift(path_root):
    contents_0 = os.listdir(path_root)
    for i in range(len(contents_0)):
        empty = False
        while not empty:
            contents_1 = os.listdir(path_root + contents_0[i])


def sort():

if __name__ == "__main__":
    main()
