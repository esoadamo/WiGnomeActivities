@echo off
REM Set path for you python 3.4:
set python34=c:\python34\python.exe

title Exe creator 
echo Unpacking files...
echo from base64 import b64decode; from sys import argv; f = open(argv[1], 'wt'); f.write(b64decode(argv[2].encode('ascii')).decode('utf8')); f.flush(); f.close() > debase_oneline.py
"%python34%" debase_oneline.py setup.py ZnJvbSBkaXN0dXRpbHMuY29yZSBpbXBvcnQgc2V0dXAKaW1wb3J0IHB5MmV4ZQogCnNldHVwKAogICAgd2luZG93cz1bJ3dpZ25vbWVfYWN0aXZpdGllcy5weSddLAogICAgb3B0aW9ucyA9IHsKICAgICAgICAncHkyZXhlJzogewogICAgICAgICAgICAncGFja2FnZXMnOiBbJ3B5YXV0b2d1aSddCiAgICAgICAgfQogICAgfQopCg==
"%python34%" debase_oneline.py setup2.py ZnJvbSBkaXN0dXRpbHMuY29yZSBpbXBvcnQgc2V0dXANCmltcG9ydCBweTJleGUNCnNldHVwKA0KICAgIGNvbnNvbGU9Wyd3aWdub21lX2FjdGl2aXRpZXNfcHJvZmlsZV9lZGl0b3IucHknXSwNICAgIGRhdGFfZmlsZXMgPSBbKCcnLFsnd2lnbm9tZV9hY3Rpdml0aWVzLnB5J10pXSwNCiAgICBvcHRpb25zID0gew0KICAgICAgICAncHkyZXhlJzogew0KICAgICAgICAgICAgJ3BhY2thZ2VzJzogWydweWF1dG9ndWknXQ0KICAgICAgICB9DQogICAgfQ0KKQ0NDQ0K==
del debase_oneline.py
echo Creatting exe...
"%python34%" setup.py py2exe
"%python34%" setup2.py py2exe
echo Exe created
echo Cleaning up...
del setup.py
del setup2.py
rmdir __pycache__ /s /q
echo Your exe file is located inside 'dist' folder
PAUSE