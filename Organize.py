# Organization of files in the downloads folder
# You can schedule this script to run every day at a certain time using the Windows Task Scheduler.

import os
import shutil
from dotenv import load_dotenv

# Environment variables
load_dotenv()
path = os.getenv("DOWNLOADS_DIR")

if os.path.exists(path):
    files = os.listdir(path)

    for file in files:
        extension = os.path.splitext(file)[1]

        # Skip folders
        if extension == '':
            continue

        # Create a folder with the name of the extension
        if not os.path.exists(path + '\\' + extension):
            os.mkdir(path + '\\' + extension)

        shutil.move(path + '\\' + file, path + '\\' + extension + '\\' + file)
else:
    print("Invalid path")


