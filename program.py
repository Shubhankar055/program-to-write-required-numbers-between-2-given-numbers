a = 2
b = 3
nr = 10


st = (b-a)/nr
lst = [a]

for i in range(0,nr-1):
	lst.append(lst[i]+st)
#print(lst)
nls = ['%.3f' % elem for elem in lst]
print(nls)

