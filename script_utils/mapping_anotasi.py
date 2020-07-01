import random, sys, os, json

workdir = os.getcwd()

data_anot = []
file1 = open(workdir + '/' + str(sys.argv[1]), 'r')
Lines = file1.readlines()

for line in Lines:
	data_anot.append(line.replace('\n',''))

file1 = open(workdir + '/' + str(sys.argv[2]), 'r')
Lines = file1.readlines()

data_name = []
for line in Lines:
	data_name.append(line.replace('\n',''))

anotasi = []
for name in data_name:
	info = {"caption":random.choice(data_anot),"image_id":name}
	anotasi.append(info)

with open(workdir + '/' + str(sys.argv[3]), 'w') as fp:
    json.dump(anotasi, fp)

