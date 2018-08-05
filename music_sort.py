#!/usr/bin/env python

import os, sys, unicodedata, shutil     # native utilities
import eyed3    # audio file ID3 package

def main():
    if os.getcwd() != '/':
        os.chdir('/')
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')
    print('~~~~~~~~~~~~~~~~~~  MUSIC SORTER  ~~~~~~~~~~~~~~~\n')
    print('~~~~~~~~~~~  Northwestern University  ~~~~~~~~~~~\n')
    path_root = str(raw_input('Please enter destination folder:'))
    # Setup detection/expansion of '~' home shortcut
    # path cleanup:
    if path_root.find('~') != -1: # Expand ~ to /home/<user>
        path_root = os.path.expanduser(path_root)
    if path_root[-1] != '/': # Append missing slash
        path_root += '/'
    if not os.path.exists(path_root): # Check for existance
        print('ERROR: The path you input could not be found\n')
        print('Exiting...')
        return
    print('Creating destination folder at ' + path_root + '_sorted')
    os.makedirs(path_root + '_sorted')

def sift(path_root):
    for object in os.listdir(path_root):
        file_found = 0
        cur_path = None
        while not file_found:
            if

def sort():
