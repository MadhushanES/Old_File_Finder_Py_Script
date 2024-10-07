import os
from datetime import datetime, timedelta

# directory to scan
base_dir = raw_input('Enter path to your directory: ')  
num_days = int(raw_input('Enter number of days: ')) 

# cutoff time
cutoff_time = datetime.now() - timedelta(days=num_days)

def list_old_folders(base_dir, cutoff_time):
    # Traverse the directory tree
    for foldername, subfolders, filenames in os.walk(base_dir, topdown=False):
        # Get the folder's last modification time
        folder_mtime = datetime.fromtimestamp(os.path.getmtime(foldername)) 
        
        # Check if the folder is older than the cutoff time
        if folder_mtime < cutoff_time:
            print("Folder {} is older than {} days (modified on {})".format(foldername, num_days, folder_mtime))

# Run the function
list_old_folders(base_dir, cutoff_time)
