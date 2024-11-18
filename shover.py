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
import datetime


source_path = "/srv/video/chapel/"
transfer_path = "/srv/video/transfer/"
target_path = "/srv/ifs/"
video_extension = ".flv"

videos = {}
file_list = os.listdir(source_path)
for file_name in file_list:
    if file_name[-4:] == video_extension:
        videos[video_name] = os.path.getmtime(source_path+video_name)
print(videos)

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