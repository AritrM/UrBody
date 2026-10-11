#medi.py
import json
import time
import threading

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
        print(self.remindata)

    def show(self):
        for x in self.data:
            print(x["name"])

    def add(self):
        name = input("Medicine name: ")
        use = input("Medicine use: ")
        medtype = input("daily/weekly/monthly/...: ")
        startDate = f"{time.localtime().tm_year}-{time.localtime().tm_mon}-{time.localtime().tm_mday}"
        print(startDate)
        expiryDate = input("Enter the expiry date of the medicine (in YYYY-MM-DD format): ")
        print(expiryDate)
        frequency = int(input("Medicine frequency: "))
        mtime = {}
        print("Fill the time slot (in HH:MM format)")
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
            for j in range(l):
                print(self.data[i]['time'][f'{j}'])

    def notify(self):
        while True:
            t = time.localtime().tm_hour * 60 + time.localtime().tm_min
            # print(t)
            for i in range(self.size):
                for x in self.remindata[self.data[i]['name']]:
                    # print(x,t)
                    if x-t < 200:
                        print("Medicine time:",self.data[i]['name'])
            time.sleep(60)
            if self.CSIGNAL == 1:
                break
            print("working")

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
