n = int(input())
temp=n
binary = []
while temp!=0:
	a = temp%2
	binary.append(a)
	temp=temp/2
len = len(binary)
count=0
for i in range(0,len):
	if binary[i]==0:
		count=0
	else:
		count+=1
print(count)
