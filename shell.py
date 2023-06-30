from os import system

cmd = input("$ ")
if cmd == 'install':
    system("cd commands")
    system("./install.sh")
if cmd == 'rotate':
    system("cd commands")
    system("python3 rotate.py")