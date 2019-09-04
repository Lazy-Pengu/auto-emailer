import os
import sys
import platform

if platform.system() != "Windows":
    sys.exit("Must be Windows machines")

file_path = '"{}"'.format(os.path.abspath('main.py'))
prompt_off = "@ECHO off\n"

bat_body = prompt_off + "python " + file_path
with open('[17].bat', 'w') as file:
    file.write(bat_body)
    file.close()