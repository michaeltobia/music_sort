#!/usr/bin/env python

import os, sys, unicodedata, shutil     # native utilities
import eyed3    # audio file ID3 package

def main():
    for filename in os.listdir('.'):
        if os.path.isdir(filename):
            if len(os.listdir(filename))==1:
                pass # skip if dir is sorted already
                ##############################
                # CHECK IF INTERIOR DIR MATCHES ALBUM NAME
                # CHECK IF _MACOSX DIR
                #   DELETE IF _MACOSX DIR,

            elif len(os.listdir(filename)) > 1:
                check = sort_dir(filename)
                if check=
            else:
                # delete empty dir
        else:
            pass

#tasks:
#   Check if cur_path is an image
#   Check cur_path metadata
#   Create album dir and move files to album dir
#   Change current_dir to cur_path.tag.artist
#   Double check cur_path.tag.album over multiple files (LATER)
#       Multiple checks should be possible unless file only includes cover
#       and one song
def sort_dir(current_dir):
    album = False   # False for initial run, replaced with string
    for content in os.listdir(current_dir): # for every file in current_dir
        cur_path = current_dir + '/' + content # form file path
        if 'jpg' in cur_path or 'png' in cur_path or 'jpeg' in cur_path:
            pass # skip sort if album art
        elif 'pdf' in cur_path or 'txt' in cur_path or 'ini' in cur_path:
            pass # skip sort if document
        elif '__MACOSX' in cur_path:
            print "Warning, folder" + current_dir + "is __MACOSX!"
            return "OSX ERROR"
        elif 'mp3' in cur_path:
            try:
                metadata = eyed3.load(cur_path)
            except UnicodeDecodeError:
                print "File " + cur_path + " caused a decoding error"
                return "UNICODE ERROR"
            if not album:
                album = unicodedata.normalize('NFKD', metadata.tag.album).encode('ascii','ignore')
                artist = unicodedata.normalize('NFKD', metadata.tag.artist).encode('ascii','ignore')
                continue
            else:
                check = album == unicodedata.normalize('NFKD', metadata.tag.album).encode('ascii','ignore')
                if check:
                    dir_path = "./" + current_dir + '/' + album
                    os.mkdir(dir_path) # defaults to full permissions
                    for song2mv in os.listdir(current_dir):
                        if os.path.isdir(song2mv):
                            pass
                        else:
                            cur_song = "./" + current_dir + '/' + song2mv
                            shutil.move(cur_song, dir_path)
                os.rename(current_dir, artist)
                return 0
        else:
            print "WARNING: " + current_dir + " contains unknown file type"
            return "Unknown File Type"








if __name__ == "__main__":
    main()
