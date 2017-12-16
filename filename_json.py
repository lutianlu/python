import os

for x in os.listdir(r'C:\Users\ThinkPads\Desktop\七期结业学员'):
    print(x)

z = []
y = ['name', 'job', 'No', 'photo']
with open(r'C:\Users\ThinkPads\Desktop\7.txt', 'r', encoding='UTF-8') as somefile:
    for line in somefile:
        n = line.split()
        n.append('/_feidike/img/old/7/' + line.split()[0] + '.jpg')
        z.append(dict(zip(y, n)))
        # print(o)
print(z)
