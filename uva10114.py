def solve():
	firstline = list(map(lambda x: float(x), input().split(" ") ))
#	print(firstline)
	carValue = firstline[2] + firstline[1]
	amountDue= firstline[2]

	depreciation = {}
	
	for i in range(int(firstline[3])):
		arr = input().split(' ')
		depreciation[int(arr[0])] = float(arr[1]) 

	depreciation[-1] = depreciation[0] 

	carValue = carValue * (1 - depreciation[0])
	for i in range(int(firstline[0])+1):
		if not i in depreciation:
			depreciation[i] = depreciation[i-1]	
	
	if carValue > amountDue:
		print('0 months')
		return
	i = 1
	while(True):
#		print(i, carValue , amountDue, carValue > amountDue)
		carValue = carValue * (1 - depreciation[i])
#		print(amountDue)
		amountDue = amountDue - (firstline[2]/firstline[0])
#		print(amountDue)
		if carValue > amountDue:
#			print('something')
			if i == 1:
				print('1 month' )
				return
			print(i, 'months')
			return
		i = i + 1
#	print('failed')
				
while True:
	try:
		solve()
	except:
		break


