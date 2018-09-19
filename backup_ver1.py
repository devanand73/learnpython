'''
How It Works
You will notice how we have converted our design into code in a step-by-step manner.

We make use of the os and time modules and so we import them. Then, we specify the files and directories to be backed up in the source list. The target directory is where store all the backup files and this is specified in the target_dir variable. The name of the zip archive that we are going to create is the current date and time which we fetch using the time.strftime() function. It will also have the .zip extension and will be stored in the target_dir directory.

The time.strftime() function takes a specification such as the one we have used in the above program. The %Y specification will be replaced by the year without the cetury. The %m specification will be replaced by the month as a decimal number between 01 and 12 and so on. The complete list of such specifications can be found in the [Python Reference Manual] that comes with your Python distribution. Notice that this is similar to (but not same as) the specification used in print statement (using the % followed by tuple).

We create the name of the target zip file using the addition operator which concatenates the strings i.e. it joins the two strings together and returns a new one. Then, we create a string zip_command which contains the command that we are going to execute. You can check if this command works by running it on the shell (Linux terminal or DOS prompt).

The zip command that we are using has some options and parameters passed. The -q option is used to indicate that the zip command should work quietly. The -r option specifies that the zip command should work recursively for directories i.e. it should include subdirectories and files within the subdirectories as well. The two options are combined and specified in a shorter way as -qr. The options are followed by the name of the zip archive to create followed by the list of files and directories to backup. We convert the source list into a string using the join method of strings which we have already seen how to use.

Then, we finally run the command using the os.system function which runs the command as if it was run from the system i.e. in the shell - it returns 0 if the command was successfully, else it returns an error number.

Depending on the outcome of the command, we print the appropriate message that the backup has failed or succeeded and that's it, we have created a script to take a backup of our important files!


'''

#!/usr/bin/python
# Filename: backup_ver1.py

import os
import time

# 1. The files and directories to be backed up are specified in a list.
source = ['/Users/devanand/documents']
# If you are using Windows, use source = [r'C:\Documents', r'D:\Work'] or something like that

# 2. The backup must be stored in a main backup directory
target_dir = '/Users/devanand/my_backup/' # Remember to change this to what you will be using

# 3. The files are backed up into a zip file.
# 4. The name of the zip archive is the current date and time
target = target_dir + time.strftime('%Y%m%d%H%M%S') + '.zip'

# 5. We use the zip command (in Unix/Linux) to put the files in a zip archive
zip_command = "zip -qr '%s' %s" % (target, ' '.join(source))

# Run the backup
if os.system(zip_command) == 0:
	print ('Successful backup to', target)
else:
	print ('Backup FAILED')