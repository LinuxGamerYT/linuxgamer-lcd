from os import system

rotation = input
if rotation <=360:
    system("cd LCD-show/")
    system("sudo ./rotate.sh", rotation)