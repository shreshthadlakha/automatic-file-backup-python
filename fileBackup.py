# we install the pip module - "Schedule" which will help is in automating file backup
import os
import shutil
import datetime
import schedule
import time

sourceDirectory = "S:\Books to read"
destinationDirectory = "S:\Backups"

def copyFolder(source, destination):
    thisDay = datetime.date.today() # will give us the current date
    directoryDestination = os.path.join(destination, str(thisDay))
    # "Backups/09/04/2025"

    # let's catch some errors
    try:
        shutil.copytree(source, directoryDestination)     # copy everything recursively inside the destination folder
        print(f"Folder copied to: {directoryDestination}")
    except FileExistsError:
        print(f"Folder already exists in: {destination}") # when I try to copy from source directory, the files or data is already there in the destination

# now we want the backup to run every single day automatically
schedule.every().day.at("21:02").do(lambda: copyFolder(sourceDirectory, destinationDirectory)) # we specify time when we want to add backup everyday
# the above line will call the function on behalf of the user (me) everyday and do run the backup
# the .do function takes the function I want to call so here I have used Lambda

# There is another way to do it without using lambda function
""" 
def l():
    copyFolder(sourceDirectory, destinationDirectory)
schedule.every().day.at("6:55").do(l)
"""

while True:
    schedule.run_pending()
    time.sleep(60) # here 60 is that the program will sleep for 60 seconds that is - every 1 minute the program will check if the program has been run or pending task are there or not
    # if task has to be run, program will run it but if not then it won't
# when we schedule task at given time each day, but the program and computer will not run the task until we have a run_pending task scheduled. Therefore, we run it inside the while loop consistently which will look for any pending tasks, already scheduled but haven't not been run. 

# copyFolder(sourceDirectory, destinationDirectory)