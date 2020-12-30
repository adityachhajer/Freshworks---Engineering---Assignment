import json
from threading import *
import time

class model:
    def __init__(self):
        self.data = {}

    def createoper(self,key, value, timee=0):
        if key in self.data.keys():
            print("Error..This ", key, " is already present..")
        else:
            if key.isalpha():
                if ((len(self.data) < 1024 * 1024 * 1024) and (len(value) <= (1024 * 1024 * 16))):
                    if time == 0:
                        new = [value, timee]
                    else:
                        new = [value, time.time() + timee]
                    if len(key) <= 32:
                        self.data[key] = new
                else:
                    print("Error..Memory limit exceeded..")

            else:
                print("Error..Key must contain only string values..")

        return

    def read(self,key):
        if key not in self.data.keys():
            print("Error..",key," does not exists in database..")
        else:
            val=self.data[key]
            if val[1]!=0:
                if time.time()<val[1]:
                    print(str(key)+":"+str(val[0]))
                else:
                    print("Error..",key," has expired..")
            else:
                print(str(key)+":"+str(val[0]))
        return


    def deleteop(self,key):
        if key not in self.data.keys():
            print("Error..",key," does not exists in database..")
        else:
            val = self.data[key]
            if val[1] != 0:
                if time.time() < val[1]:
                    del self.data[key]
                    print("Key is deleted successfully..")
                else:
                    print("Error..", key, " has expired..")
            else:
                del self.data[key]
                print("Key is deleted successfully..")
        return

    def adddata(self,path):
        with open(path,'r') as f:
            xd = json.load(f)
        for i in xd:
            self.data[i[0]]=i[1]
        return

    def makenewfile(self):
        with open('file.json', 'w') as f:
            for i in self.data.items():
                json.dump(i, f)
        return
