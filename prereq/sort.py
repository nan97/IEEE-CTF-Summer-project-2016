names=["nandini","dhir","swati","sreeps","rohanSurve","tarun","chinmaydd","sarthak","swathibhat","natasha"]
for x in range(0,9):
	for y in range(x+1,10):
		if(names[x]>names[y]):
			t=names[x];
			names[x]=names[y]
			names[y]=t
for x in range(0,10):
	print(names[x])

