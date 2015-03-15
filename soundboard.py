#!/opt/local/bin/python

from __future__ import print_function

import os
from os import path

DIRECTORY = "./sounds"

def read_in_sounds(sound_dir, include_it) :
    for root, dirs, files in os.walk(sound_dir) :
        for afile in files :
            if include_it(root, afile) :
                yield path.join(root, afile)

def is_int(s) :
   try :
       int(s)
       return True
   except ValueError:
       return False


def main(sound_dir, sound_player, file_filter) :
    values = list(enumerate(read_in_sounds(sound_dir, file_filter)))
    lookup = dict(values)
    done = False
    while not done :
        for i, sound in values :
            print("%i) %s" % (i, sound))
        print("'q(uit)' to quit")
        choice = raw_input("Enter your choice: ").lower()
        if choice == "q" or choice == "quit" :
            done = True
        elif is_int(choice) and int(choice) in lookup :
            file_to_play = lookup[int(choice)]
            sound_player(file_to_play)
        else :
            print("Unknown input %s" % choice)
    print("Good bye")

if __name__ == "__main__" :
    main(DIRECTORY, lambda x : print("playing %s" % x), lambda root, path : True)

