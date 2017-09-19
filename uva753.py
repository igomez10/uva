def solve():
	aline = list(map(lambda x: int(x), input().split(" ") ))
	if aline[0] == 0:
		return
	
	currentDay = 1
	currentPosition = 0
	currentRate = aline[1]
	while(True):
	# print('start position', currentPosition)
		currentPosition = currentPosition + currentRate
	# print('climbed to', currentPosition)
	# print('current rate', currentRate)
	
		currentRate =  aline[1] * (1 - (currentDay * (aline[3] / 100)))
		if currentRate < 0:
			currentRate = 0 
		if currentPosition > aline[0]:
			print('success on day' , currentDay)
			break
		if currentPosition < 0:
			print('failure on day', currentDay)
			break

		currentPosition = currentPosition - aline[2]
	
		if currentPosition < 0:
			print('failure on day', currentDay)
			break
		currentDay = currentDay + 1
	
while(True):
	try:
		solve()
	except:
		break