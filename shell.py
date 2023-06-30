from os import system

cmd = input("$ ")
if cmd == 'install':
    system("sudo chmod +x install.sh")
    system("./install.sh")
if cmd == 'rotate':
    system("python3 rotate.py")
