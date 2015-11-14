#!/usr/bin/env python

import os
from os.path import expanduser
import subprocess

home = expanduser("~")
if not os.path.exists(home+"/Library/Application Support/Kodi/userdata"):
	os.makedirs(home+"/Library/Application Support/Kodi/userdata")
	print "Created Kodi 'userdata' Directory"

data = "<advancedsettings>\n  <videodatabase>\n    <type>mysql</type>\n    <host>X.X.X.X</host>\n    <port>3306</port>\n    <user>kodi</user>\n    <pass>kodi</pass>\n  </videodatabase>\n  <musicdatabase>\n    <type>mysql</type>\n    <host>X.X.X.X</host>\n    <port>3306</port>\n    <user>kodi</user>\n    <pass>kodi</pass>\n  </musicdatabase>\n  <videolibrary>\n    <importwatchedstate>true</importwatchedstate>\n    <importresumepoint>true</importresumepoint>\n  </videolibrary>\n  <network>\n    <buffermode>1</buffermode>\n    <cachemembuffersize>20971520</cachemembuffersize>\n    <readbufferfactor>10</readbufferfactor>\n  </network>\n</advancedsettings>"
the_command = "/usr/bin/touch "+home+"\"Library/Application Support/Kodi/userdata/advancedsettings.xml\""
p=subprocess.Popen(the_command,shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE)

print "Writing Kodi Advanced Settings"
os.chdir(home)
file = open("Library/Application Support/Kodi/userdata/advancedsettings.xml", "w")
file.write(data)
file.close()
 
print "Done"