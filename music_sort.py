#!/usr/bin/env python

### Might need to put this all in a class to get the destination folder path to
### nicely transfer from main() to sort()

import os, sys, unicodedata, shutil     # native utilities
import eyed3    # audio file ID3 package

class MusicSorter:
    def __init__(self):
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')
        print('~~~~~~~~~~~~~~~~~~  MUSIC SORTER  ~~~~~~~~~~~~~~~\n')
        print('~~~~~~~~~~~  Northwestern University  ~~~~~~~~~~~\n')
        self.path_root = str(raw_input('Please enter destination folder:'))
        # Setup detection/expansion of '~' home shortcut
        # path cleanup:
        if os.getcwd() != '/':
            print("Changing working directory to '/'...\n")
            os.chdir('/')
        if self.path_root.find('~') != -1: # Expand ~ to /home/<user>
            self.path_root = os.path.expanduser(self.path_root)
        if not os.path.exists(self.path_root): # Check for existance
            print('ERROR: The path you input could not be found\n')
            print('Exiting...')
            return
        try:
            self.path_dest = self.path_root + '_sorted'
            os.makedirs(self.path_dest) # make destination folder
            print('Created destination folder at ' + self.path_dest)
        except OSError:# or use existing dest' folder
            print('Using existing destination folder at ' + self.path_dest)
        print('Begning sort...')
        self.sift(self.path_root)
        # print('TEST COMPLETE')
        # return

    def sift(self, path):
        contents = os.listdir(path)
        if len(contents) == 0:
            print('\n\n\n****EMPTY: ' + path + '\n\n\n')
            # os.rmdir(path)
        for i in range(len(contents)):
            print i
            cur_path = path + '/' + contents[i]
            if os.path.isdir(cur_path) and (contents[i][0] != '_'):
                # print "NEW DIR: " + contents[i]
                self.sift(cur_path)
            else:
                self.sort(cur_path)
                # if contents[i].find('.mp3') != -1:
                #
                #     # print "SONG: " + contents[i]
                # elif contents[i].find('.png') != -1 or contents[i].find('.jpg') != -1:
                #     # print "COVER: " + contents[i]
                #     continue
                #     ## Figure out a better way to sort covers
                # elif contents[i].find('.ini') != -1:
                #     continue
                #     # print "ERROR: " + contents[i]


    def sort(self, path):
        if path.find('.mp3') != -1:
            try:
                cur_song = eyed3.load(path)
                self.cur_artist = cur_song.tag.artist
                self.cur_album = cur_song.tag.album
                print(self.cur_artist + ': ' + self.cur_album)
            except UnicodeDecodeError:
                print('ERROR: Unicode error at ' + path)
                return
        elif path.find('.png') != -1 or path.find('.jpg') != -1:
            print('COVER: ' + path + '\n')
        else:
            print('TRASH: ' + path + '\n')
        return


if __name__ == "__main__":
    main()
