import csv

def acc_areterial(s1,s2):
	count1 = 0
	f1 = []
	f2 =[]
	for i in s1:
		if(i['ACCESSIBLE'] == 'Accessible'):
			f1.append(i['FDMID'])
	for j in s2:
		if (j['ST_CLASS']=='ARTERIAL'):
			f2.append(j['FDMID'])

	for e1 in f1:
		for e2 in f2:
			if(e1==e2):
				count1+=1
	return count1

def non_local(s3,s4):
	count2 = 0
	f3 = []
	f4 =[]
	for i in s3:
		if(i['ACCESSIBLE'] == 'Non-Standard'):
			f3.append(i['FDMID'])
	for j in s4:
		if (j['ST_CLASS']=='LOCAL STREET'):
			f4.append(j['FDMID'])

	for e3 in f3:
		for e4 in f4:
			if(e3==e4):
				count2+=1
	return count2

def in_minor(s5,s6):
	count3 = 0
	f5 = []
	f6 =[]
	for i in s5:
		if(i['ACCESSIBLE'] == 'Inaccessible'):
			f5.append(i['FDMID'])
	for j in s6:
		if (j['ST_CLASS']=='MINOR COLLECTOR'):
			f6.append(j['FDMID'])

	for e5 in s5:
		for e6 ins:
			if(e5==e6):
				count3+=1
	return count3




a_bus= open("Bus_Stops.csv")
a_street = open("Street_Centrelines.csv")

s1 = csv.DictReader(a_bus)
s2 = csv.DictReader(a_street)

print(acc_areterial(s1,s2))
print(non_local(s1,s2))
print(in_minor(s1,s2))

