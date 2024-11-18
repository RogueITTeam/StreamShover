#!/usr/bin/python3

##
 # StreamShover
 # Copyright (C) 2024 St Edmund's College at the University of Cambridge
 #
 # StreamShover is free software: you can redistribute it and/or modify
 # it under the terms of the GNU Affero General Public License as published by
 # the Free Software Foundation, version 3 of the License.
 #
 # StreamShover is distributed in the hope that it will be useful,
 # but WITHOUT ANY WARRANTY; without even the implied warranty of
 # MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 # GNU General Public License for more details.
 #
 # You should have received a copy of the GNU General Public License
 # along with StreamShover.  If not, see <https://www.gnu.org/licenses/>.
##

"""
Things we'll need:
os.path.getmtime - File epoch
time.time() - Now epoch.
3600 - One hour of seconds.
"""

import os
import shutil
import time as time


source_path = "/srv/video/chapel/"
transfer_path = "/srv/video/transfer/"
target_path = "/srv/ifs/"
video_extension = ".flv"

print("Found the following recordings:")
videos = {}
file_list = os.listdir(source_path)
for file_name in file_list:
    if file_name[-4:] == video_extension:
        videos[file_name] = os.path.getmtime(source_path+file_name)
        print(file_name)
print()

for video, age in videos.items():
    print("Checking:", video)
    now = time.time() + 3600
    if (age < (now)):
        print("Moving:", video)
        try:
            shutil.move(source_path+video, transfer_path+video)
        except Exception as error_message:
            print("Something went wrong moving:", video, "from", source_path, "to", transfer_path, "-", error_message)
            continue
        print("Copying:", video)
        try:
            shutil.copy(transfer_path+video, target_path+video)
        except Exception as error_message:
            print("Something went wrong copying:", video, "from", transfer_path, "to", target_path, "-", error_message)





"""
if (video/file.age > 1 hour):
    os.move video//chapel/file video/transfer/file
    os.copy video/transfer/file ifs/file
    if (error):
        email Espen
        break
    if (md5sum(video/transfer/file) == md5sum(ifs/file)):
        delete(video/transfer/file)
        email Alex
    else
        email Espen
"""
