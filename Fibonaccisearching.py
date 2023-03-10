import os
os.system("cls")

print ("""
==================================================================================================================
|                                   Nama      : Aufa Tri Hapsari                                                 |
|                                   NIM       : 2209116031                                                       |
|----------------------------------------------------------------------------------------------------------------|
|                                      Posttest 2 ASD Searching                                                  |
==================================================================================================================               
""")

def dataaslab():
    for i in range(len(Dataset)):
        if type (Dataset[i]) != str:
            data2[i] = Dataset[i]
        else:
            data1.append(Dataset[i])          
    for j in data2:
        data1.insert(j, data2[j])
    print("".center(70,"="))
    print("Data nama aslab:", data1)
    print("".center(70,"="))

#searching
def fibonacci(e, x, o):
    searching1 = 0
    searching2 = 1
    fibonacci = searching1 + searching2
    while (fibonacci < o):
        searching1 = searching2
        searching2 = fibonacci
        fibonacci = searching1 + searching2
    offset = -1
    while (fibonacci > 1):
        i = min(offset + searching1, o-1)
        if (e[i] < x):
            fibonacci = searching2
            searching2 = searching1
            searching1 = fibonacci - searching2
            offset = i
        elif (e[i] > x):
            fibonacci = searching1
            searching2 = searching2 - searching1
            searching1 = fibonacci - searching2
        else:
            return i
    if (searching2 and e[o-1] == x):
        return o-1
    return -1
    
def search():
    print("Mencari Kata", x )
    print("kata", x, "ditemukan pada = ")
    for z in range(len(data1)):
        if type(data1[z]) == list:
            kolomdata = fibonacci(Dataset[z], x, len(Dataset[z]))
            print(x, "berada di array index ke :",z,"kolom",kolomdata)
            return
        else:
            if data1[z] == x:
                print(x, "berada di array index ke : ",z)
                return
                
Dataset = ["Arsel", "Avivah", "Daiva", ["Wahyu", "Wibi"]]
data1 = []
data2 = {}

dataaslab()
x = "Arsel"
search()
print("".center(70,"="))
x = "Avivah"
search()
print("".center(70,"="))
x = "Daiva"
search()
print("".center(70,"="))
x = "Wahyu"
search()
print("".center(70,"="))
x = "Wibi"
search()
print("".center(70,"="))