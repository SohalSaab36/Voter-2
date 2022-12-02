import os
import time

SEC =    time.time()
def getTime():
    return time.ctime(SEC)
def getTimeNS():
    lat =    time.ctime(SEC)
    return ''.join(lat.split())
def    TouchWrite(file,DBS):
    f= open(file,"w+")
    f.write(DBS)
    f.close()
def getRoot():
    return os.getcwd()
def createLogFolder(folder,root):
    os.chdir(root)
    os.mkdir(folder)
def chdir(Dest):
    os.chdir(Dest)
def pathCheck(path):
    Path =    str(path)
    return os.path.exists(Path)