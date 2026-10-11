#medi.py
import json
import time
import threading
from notifypy import Notify

class Medicine:
    def __init__(self):
        mfile = open("medfile.json","r")
        self.rawdata = json.load(mfile)
        self.data = self.rawdata['medicine']
        self.size = len(self.data)
        self.remindata = {}
        self.CSIGNAL = 0
        self.timelog()
        mfile.close()

    def timelog(self):
        for i in range(self.size):
            l = self.data[i]['frequency']
            self.remindata[self.data[i]['name']] = []
            for j in range(l):
                tstring = self.data[i]['time'][f'{j}'].partition(':')
                t = int(tstring[0]) * 60 + int(tstring[2])
                self.remindata[self.data[i]['name']].append(t)

    def show(self):
        i = 0
        for x in self.data:
            i+=1
            print(i,x["name"])

    def add(self):
        name = input("Medicine name: ")
        use = input("Medicine use: ")
        medtype = input("daily/weekly/monthly/...: ")
        startDate = f"{time.localtime().tm_year}-{time.localtime().tm_mon}-{time.localtime().tm_mday}"
        expiryDate = input("Enter the expiry date of the medicine (in YYYY-MM-DD format): ")
        frequency = int(input("Medicine frequency: "))
        mtime = {}
        if frequency > 0:
            print("Fill the time slot (in HH:MM format)")
        else:
            print("Invalid! Frequency set to 0.")
            frequency = 0
        for i in range(frequency):
            mtime[f"{i}"] = input(f"{i}: ")
        info = {
                'name':name,
                'use':use,
                'type':medtype,
                'startDate':startDate,
                'expiryDate':expiryDate,
                'time':mtime,
                'frequency': frequency
                }
        self.data.append(info)

    def save(self):
        fw = open("tmp.json","w")
        json.dump(self.rawdata,fw)
        fw.close()
        print(self.data)
        print("Saved!")

    def checkup(self):
        for i in range(len(self.data)):
            l = self.data[i]['frequency']
            print(self.data[i]['name'],end="\t")
            for j in range(l):
                print(self.data[i]['time'][f'{j}'],end=",\t")
            print()

    def notify(self):
        while True:
            tmin = time.localtime().tm_hour * 60 + time.localtime().tm_min
            for i in range(self.size):
                for x in self.remindata[self.data[i]['name']]:
                    # print(x,t)
                    if x-tmin < 5:
                        print("Medicine time:",self.data[i]['name'])
            if self.CSIGNAL == 1:
                break
            notification = Notify()
            notification.title = "Alert"
            notification.message = "Medicine time!"
            notification.send()
            time.sleep(60)

    def fquit(self):
        self.CSIGNAL = 1

def med():
    print("See your medicines...")
    medlist = Medicine()
    thread = threading.Thread(target=medlist.notify, args=())
    thread.start()
    while True:
        c = input("Enter your choice: ")
        if c == 's':
            medlist.show()
        elif c == 'a':
            medlist.add()
        elif c == 'w':
            medlist.save()
        elif c == 'c':
            medlist.checkup()
        elif c == 'q':
            print("Exited!")
            medlist.fquit()
            exit(0)
        else:
            print("Wrong choice!")

med()
