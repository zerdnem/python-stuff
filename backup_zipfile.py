import os
import time
import zipfile
import sys 

source = sys.argv[1]

target_dir = "/Users/jjan/backup"

if not os.path.exists(target_dir):
    os.mkdir(target_dir)

today = target_dir + os.sep + time.strftime("%Y%m%d")

now = time.strftime("%H%M%S")

comment = raw_input("Enter a comment --> ")

target = today + os.sep + now + "_" + \
            comment.replace(" ", "_") + ".zip"

if not os.path.exists(today):
    os.mkdir(today)

try:
    relroot = os.path.abspath(os.path.join(source, os.pardir))
    with zipfile.ZipFile(target, "w", zipfile.ZIP_DEFLATED) as zip:
        for root, dirs, files in os.walk(source):
            # add directory (needed for empty dirs)
            zip.write(root, os.path.relpath(root, relroot))
            for file in files:
                filename = os.path.join(root, file)
                if os.path.isfile(filename): # regular files only
                    arcname = os.path.join(os.path.relpath(root, relroot), file)
                    zip.write(filename, arcname)
    print "Successful backup to", target
except:
    print "Backup FAILED"
