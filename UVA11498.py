
def solve():
	numCases = int(input())	
#	print('numcases', numCases)
	thec = input()
#	print(thec.split(' '))
	center = list(map( lambda x: int(x) , thec.split(" ") )) 
	for i in range(numCases):
		current = input()
#		print('----', current)
		coord = list(map( lambda x: int(x) , current.split(" ") ))
		result = []
		if coord[0] == center[0] or coord[1] == center[1]:
			print('divisa')
			continue
		if coord[1] > center[1]:
			result.append('N')
#			print('N coord[1]:' , coord[1] , ' > ' , center[1], 'center1')
		else:
			result.append('S')
#			print('S coord[1]:' , coord[1] , ' < ' , center[1], 'center1')
		if coord[0] > center[0]:
			result.append('E')
#			print('E coord[0]:' , coord[0] , ' > ' , center[0], 'center0')   
		else:
			result.append('O')
#			print('W coord[0]:' , coord[0] , ' > ' , center[0], 'center0')
		print(result[0] + result[1])
	
	
while(True):
	try:
		solve()
	except:
		break
		