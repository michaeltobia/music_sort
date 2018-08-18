#!/usr/bin/env python

import os, sys, unicodedata, shutil     # native utilities
import eyed3    # audio file ID3 package

class MusicSorter:
    def __init__(self):
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')
        print('~~~~~~~~~~~~~~~~~~  MUSIC SORTER  ~~~~~~~~~~~~~~~\n')
        print('~~~~~~~~~~~  Northwestern University  ~~~~~~~~~~~\n')
        self.path_root = str(raw_input('Please enter target folder:'))
        # (DONE) Setup detection/expansion of '~' home shortcut
        # Setup dryrun:
        self.dry_run = str(raw_input('Dry run? (y/n)'))
        if self.dry_run != 'n':
            self.dry_run = 'y' # Default to dry run on inappropriate input
        print("Dry run status: " + self.dry_run)
        self.sort_log = {}
        self.duplicate_name_counter = 0
        # path cleanup:
        print('You entered: ' + self.path_root)
        if os.getcwd() != '/':
            print("Changing working directory to '/'...\n")
            os.chdir('/')
        if self.path_root.find('~') != -1: # Expand ~ to /home/<user>
            self.path_root = os.path.expanduser(self.path_root)
        if not os.path.exists(self.path_root): # Check for existance
            print('ERROR: The path you input could not be found\n')
            print('Exiting...')
            return
        try: # make destination folder
            self.path_dest = self.path_root + '/_sorted'
            os.makedirs(self.path_dest)
            print('Created destination folder at ' + self.path_dest)
        except OSError: # or use existing dest' folder
            print('Using existing destination folder at ' + self.path_dest)
        try: # make error folder
            self.path_error = self.path_dest + '/_unsorted'
            os.makedirs(self.path_error)
        except OSError: # or use existing error folder
            pass
        print('Begning sort...')
        print(self.path_root)
        self.sift(self.path_root)
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
        if self.dry_run == 'n':
            os.rmdir(path)
        self.return_log()

    # Still has trouble with split albums (albums that have multiple artists)
    def sort(self, path):
        if path.find('.mp3') != -1:
            try:
                cur_song = eyed3.load(path)
                self.cur_artist = cur_song.tag.artist
                self.cur_album = cur_song.tag.album
                self.cur_title = cur_song.tag.title
                self.cur_artist_path = self.path_dest + '/' + self.cur_artist
                self.cur_album_path = self.cur_artist_path + '/' + self.cur_album
                # print(self.cur_album_path)
                # print(self.cur_artist + ': ' + self.cur_album + ': ' + self.cur_title)

                ## Check if dest folders exist
                if self.dry_run == 'n':
                    if not os.path.exists(self.cur_artist_path):
                        # make artist folder if it doesn't exist
                        os.makedirs(self.cur_artist_path)
                    if not os.path.exists(self.cur_album_path):
                        # make album folder if it doesn't exist
                        os.makedirs(self.cur_album_path)
                    # move song to album path
                    try:
                        shutil.move(path, self.cur_album_path)
                    except shutil.Error:
                        shutil.move(path, self.path_error)
                        print("Duplicate error at: " + path)


                #Add song to sort_log
                if self.cur_artist in self.sort_log:
                    if self.cur_album in self.sort_log[self.cur_artist]:
                        self.sort_log[self.cur_artist][self.cur_album].append(self.cur_title)
                    else:
                        self.sort_log[self.cur_artist][self.cur_album] = [self.cur_title]
                else:
                    self.sort_log[self.cur_artist] = {}
                    self.sort_log[self.cur_artist][self.cur_album] = [self.cur_title]

            except UnicodeDecodeError:
                # if tags have indecipherable characters, move song to _unsorted
                print('ERROR: Unicode error at ' + path)
                if self.dry_run == 'n':
                    shutil.move(path, self.path_error)

                return
            except ValueError:
                print('VALUE ERROR')

        elif (path.find('.png') != -1) or (path.find('.jpg') != -1) or (path.find('.pdf') != -1):
            # Move cover or book file to cur_album dest folder
            # print('COVER: ' + path + '\n')
            if self.dry_run == 'n':
                try:
                    shutil.move(path, self.cur_album_path)
                except AttributeError:
                    shutil.move(path, self.path_error)
                    print('UNSORTED COVER: ' + path)
        else:
            # move misc files (a la .ini, .txt, ect.) to _unsorted
            # print('TRASH: ' + path + '\n')
            if self.dry_run == 'n':
                try:
                    shutil.move(path, self.path_error)
                except shutil.Error:
                    shutil.move(path, path + str(self.duplicate_name_counter))
                    shutil.move(path + str(self.duplicate_name_counter), self.path_error)
                    self.duplicate_name_counter += 1
        return

    def return_log(self):
        return self.sort_log


if __name__ == "__main__":
    MusicSorter()
