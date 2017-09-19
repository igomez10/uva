import sys
def solve(acount):
	firstLine = list(map(lambda x: int(x) , input().split(' ')))
	if not firstLine[0] == 0:
		reqs = []
		for line in range(firstLine[0]):	
			reqs.append(input())
		global bestProp 
		bestProp = [ 'name', 9999999999, 0 ]
		for aProp in range(firstLine[1]):
			name = input()
			propData = list(map(lambda x: float(x) , input().split(' ') ))
			if bestProp[2] < propData[1] or (bestProp[2] == propData[1] and propData[0] < bestProp[1] ):
				bestProp[0] = name
				bestProp[1] = propData[0]
				bestProp[2] = propData[1]
			for i in range( int(propData[1]) ):
				a = input()
		if count > 1:
			print() 
		print('RFP #' + str(acount)) 
		print(bestProp[0])
count = 0
while(True):
	try:
		count = count + 1
		solve(count)
	except:
		break
		
