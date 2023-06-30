from os import system

cmd = input("$ ")
if cmd == 'install':
    system("./install.sh")
if cmd == 'rotate':
    system("python3 rotate.py")
