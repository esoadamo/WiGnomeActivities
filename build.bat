@echo off
REM Set path for you python 3.4:
set python34=c:\python34\python.exe

title Exe creator 
echo Unpacking files...
echo from base64 import b64decode; from sys import argv; f = open(argv[1], 'wt'); f.write(b64decode(argv[2].encode('ascii')).decode('utf8')); f.flush(); f.close() > debase_oneline.py
"%python34%" debase_oneline.py setup.py ZnJvbSBkaXN0dXRpbHMuY29yZSBpbXBvcnQgc2V0dXAKaW1wb3J0IHB5MmV4ZQogCnNldHVwKAogICAgd2luZG93cz1bJ3dpZ25vbWVfYWN0aXZpdGllcy5weSddLAogICAgb3B0aW9ucyA9IHsKICAgICAgICAncHkyZXhlJzogewogICAgICAgICAgICAncGFja2FnZXMnOiBbJ3B5YXV0b2d1aSddCiAgICAgICAgfQogICAgfQopCg==
del debase_oneline.py
echo Creatting exe...
"%python34%" setup.py py2exe
echo Exe created
echo Cleaning up...
del setup.py
echo Your exe file is located inside 'dist' folder
PAUSE