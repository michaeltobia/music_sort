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
        # (DONE) Setup detection/expansion of '~' home shortcut
        # (TODO) Setup dryrun:
        self.dry_run = {}
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
        return self.dry_run
        # print('TEST COMPLETE')
        # return

    def sift(self, path):
        contents = os.listdir(path)
        ## This if statement appears to never catch empty folders because of the
        ## order this function sifts in
        if len(contents) == 0: ## Notify if current dir is empty
            print('\n\n\n****EMPTY: ' + path + '\n\n\n')
            pause_junk = input('Press enter to continue...')
            # os.rmdir(path) ## delete current folder if empty
        for i in range(len(contents)):
            cur_path = path + '/' + contents[i]
            if os.path.isdir(cur_path) and (contents[i][0] != '_'):
                # ^ Fix this if statement to more reliably detect OSX leftovers
                #  ^ Possibly use sift function ite
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
        #### Possibly place delete folder right here instead?

    # Still has trouble with split albums (albums that have multiple artists)
    def sort(self, path):
        if path.find('.mp3') != -1:
            try:
                cur_song = eyed3.load(path)
                self.cur_artist = cur_song.tag.artist
                self.cur_album = cur_song.tag.album
                self.cur_title = cur_song.tag.title
                # print(self.cur_artist + ': ' + self.cur_album + ': ' + self.cur_title)

                ## Check if dest folders exist
                if self.cur_artist in self.dry_run:
                    if self.cur_album in self.dry_run[self.cur_artist]:
                        self.dry_run[self.cur_artist][self.cur_album].append(self.cur_title)
                    else:
                        self.dry_run[self.cur_artist][self.cur_album] = [self.cur_title]
                else:
                    self.dry_run[self.cur_artist][self.cur_album] = [self.cur_title]
                ## Move cur_song to appropriate dest folder
            except UnicodeDecodeError:
                print('ERROR: Unicode error at ' + path)
                ## Move issue cur_song to error folder
                return
            except ValueError:
                ## Create artist folder
                print('Artist folder created at ' + path)
        elif (path.find('.png') != -1) or (path.find('.jpg') != -1) or (path.find('.pdf') != -1):
            print('COVER: ' + path + '\n')
            ## Move cover/book file to cur_artist+cur_album dest folder
        else:
            print('TRASH: ' + path + '\n')
            ## Delete trash files
        return


if __name__ == "__main__":
    main()
