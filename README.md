# StreamShover
Thing to move recorded streams from our server to other places.

Assumes a few hardcoded variables because I'm lazy:

* Will run hourly, and that if a file hasn't been written to in an hour, it's safe to move it.
* Streams are stored in /srv/video, are moved to /srv/video/transfer when movING, and are copied to /srv/ifs - where a .MOUNTED file tells you it's safe to copy.
