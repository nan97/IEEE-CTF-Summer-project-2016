names=["Nandini","Ragini","Vignesh","Henna"]
for x in range(0,3):
	for y in range(x+1,4):
		if(names[x]>names[y]):
			t=names[x];
			names[x]=names[y]
			names[y]=t
for x in range(0,4):
	print(names[x])

