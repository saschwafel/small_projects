#!/usr/bin/python

#Run Rsync to update local music backup from server

import sys
import os
import subprocess32 as subprocess

path = os.getcwd()

print 'Your current working dir is {}'.format(path)

#alias updatemusic="rsync -rtvu --progress --delete wizard:/home/schuyler/Downloads/MusicBackup/ /media/sschwafel/Music/MusicBackup"
user_input = raw_input('To update music with default music folder path ( /media/Music/MusicBackup ) please enter y, to enter a new path, enter n\n')

if user_input.lower() == 'y':

    print 'Your music folder is located here {}'.format('/media/Music/MusicBackup')
else:
    
    new_user_path = raw_input('What path would you like to use instead? ')

    if os.path.exists(new_user_path):
        print "The output is true!"
        sys.exit()
        #call rsync function here
    else: 
        print "That path is nonexistant"
        sys.exit()

#put this into a function
print 'Now Rsyncing your music directory from server...\n'

print '\nThis is the output of rsync with the --dry-run parameter:\n'
print subprocess.call(['rsync', '-rtvu', '--progress', '--delete', '--dry-run', 'wizard:/home/schuyler/Downloads/MusicBackup/', '/media/Music/MusicBackup'])

confirmation = raw_input("If you'd like to run the rsync command, enter y\n")

if confirmation.lower() == 'y':

    print subprocess.call(['rsync', '-rtvu', '--progress', '--delete', 'wizard:/home/schuyler/Downloads/MusicBackup/', '/media/Music/MusicBackup'])
else:
    print 'exiting...'
