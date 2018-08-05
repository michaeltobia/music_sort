#!/usr/bin/env python

### Might need to put this all in a class to get the destination folder path to
### nicely transfer from main() to sort()

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
    # if path_root[-1] != '/': # Append missing slash
    #     path_root += '/'
    if not os.path.exists(path_root): # Check for existance
        print('ERROR: The path you input could not be found\n')
        print('Exiting...')
        # return
    try:
        os.makedirs(path_root + '_sorted') # make destination folder
        print('Created destination folder at ' + path_root + '_sorted')
    except OSError:# or use existing dest' folder
        print('Using existing destination folder at ' + path_root + '_sorted')
    print('Begning sort...')
    sift(path_root)

def sift(path_root):
    contents = os.listdir(path_root)
    for i in range(len(contents)):
        cur_path = path_root + '/' + contents[i]
        if os.path.isdir(cur_path) and (contents[i][0] != '_'):
            # print "NEW DIR: " + contents[i]
            sift(cur_path)
        else:
            if contents[i].find('.mp3') != -1:
                print(cur_path)

                # print "SONG: " + contents[i]
            elif contents[i].find('.png') != -1 or contents[i].find('.jpg') != -1:
                # print "COVER: " + contents[i]
                continue
                ## Figure out a better way to sort covers
            elif contents[i].find('.ini') != -1:
                continue
                # print "ERROR: " + contents[i]


def sort(path_file):


if __name__ == "__main__":
    main()
