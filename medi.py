#medi.py
import json

class Medicine:
    def __init__(self):
        # mfile = open("medfile.json","r")
        mfile = open("tmp.json","r")
        self.data = json.load(mfile)['medicine']
        mfile.close()

    def show(self):
        for x in self.data:
            print(x["name"])

    def add(self):
        name = input("Medicine name: ")
        use = input("Medicine use: ")
        frequency = int(input("Medicine frequency: "))
        info = {
                'name':name,
                'use':use,
                'frequency': frequency
                }
        medlist.data.append(info)

    def save(self):
        fw = open("tmp.json","w")
        fw.write("{\"medicine\":[")
        for i in range(len(medlist.data)):
            fw.write("{")
            fw.write(f"\"name\": \"{medlist.data[i]['name']}\",\"use\": \"{medlist.data[i]['use']}\",\"frequency\": \"{medlist.data[i]['frequency']}\"")
            fw.write("}")
            if (i<len(medlist.data)-1):
                fw.write(",")
        fw.write("]}")
        fw.close()
        print("Saved!")

print("See your medicines...")
medlist = Medicine()
while True:
    c = input("Enter your choice: ")
    if c == 's':
        medlist.show()
    elif c == 'a':
        medlist.add()
    elif c == 'w':
        medlist.save()
    elif c == 'q':
        break
    else:
        print("Wrong choice!")

