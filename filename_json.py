import os

z = []
y = ['name', 'job', 'No', 'photo']
with open(r'C:\Users\Administrator\Desktop\7.txt', 'r', encoding='UTF-8') as somefile:
    for line in somefile:
        z.append(dict(zip(y, line.split())))

print(z)
