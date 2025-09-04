# Automatic File Backup 
_Daily file backup can be cumbersome. But this Python-based Automatic File Backup Program solves that by automating the entire process. Once set up, it silently runs in the background, copying the contents of a source folder into a backup directory at a specified time every day, at a schedule time._

## Table of Contents
<pre>
-<a href="#overview">Overview</a>
-<a href="#problem">Problem</a>
-<a href="#tools">Tools</a>
-<a href="#project-structure">Project Structure</a>
-<a href="#key-things">Key Things</a>
-<a href="#how-to-run-this-program">How to run this program</a>
-<a href="#recommendations">Recommendations</a>
-<a href="#builder-contact">Builder Contact</a>
</pre>

<h2><a class="anchor" id="overview"></a>Overview</h2>
This program is designed to:  
- Automatically back up files from a source folder to a destination folder.<br>
- Create a new dated folder every day for each backup (e.g., Backups/2025-09-04).<br> 
- Run quietly in the background using the schedule module.<br>

<h2><a class="anchor" id="problem"></a>Problem</h2>
Manual file backups are:<br>
- Easy to forget<br>
- Time-consuming<br>
- Prone to human error<br>
<br>
There was a need for a simple, hands-off solution to automate the daily backup process — especially for users who want peace of mind when dealing with critical files.

<h2><a class="anchor" id="tools"></a>Tools</h2>
- Python:- Programming language<br>
- shutil:- For copying files and directories<br>
- datetime:- For managing and formatting dates<br>
- schedule:- To automate backup tasks<br>
- time:- For checking and sleeping the loop<br>
- os:- To handle filesystem paths<br>

<h2><a class="anchor" id="projec-structure"></a>Project Structure</h2>
<pre>Automatic_File_Backup/
│
├── backup.py             # Main Python script to run the program
├── README.md             # Project documentation
</pre>

<h2><a class="anchor" id="key-things"></a>Key Things</h2>
- Daily Scheduling: Uses schedule.every().day.at("HH:MM") to run once daily.<br>
- Date-based Folders: Each backup is stored in a folder named with the current date.<br>
- Error Handling: If the folder for that day already exists, it skips the backup and notifies the user.<br>
- Modular Design: You can change the source/destination directories or backup time easily.<br>

<h2><a class="anchor" id="how-to-run-this-program"></a>How to run this program</h2>
1. Install dependencies - using # pip install schedule<br>
2. Edit script - change the time when you want to schedule the backup. The set sourceDirectory & destinationDirectory. Also set time.<br>
3. Run the script.<br>


<h2><a class="anchor" id="recommendations"></a>Recommendations</h2>
- Run this script as a startup task or create a Windows scheduled task to ensure it starts automatically.<br>
- Make sure the source and destination directories exist and are accessible.<br>
- Consider logging backup status to a .log file for better tracking.<br>
- Don’t schedule multiple backups at the same exact time.<br>
- Backup to external drives or cloud-synced folders for extra safety.<br>

<h2><a class="anchor" id="builder-contact"></a>Builder Contact</h2>

**Shreshth Adlakha**<br>
Python Developer<br>
shreshthaadlakha@gmail.com <br>
[LinkedIn](https://www.linkedin.com/in/shreshthadlakha/)
