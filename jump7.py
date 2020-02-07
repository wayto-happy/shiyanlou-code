for i in range(1,100):
	if i%7==0:
		i=i+1
	elif i%10==7:
		i=i+1
	elif i//10==7:
		i=i+1
	else:
		print(i)
