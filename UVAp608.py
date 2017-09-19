
def solve():
	listchars = {}
	realchars = []
	comparisons =[]
	counterfeit = ''
	latertosee = []
	weight = ''

	for i in range(3):
		newString = str(input())
		comparisons.append(newString)

	for comparison in comparisons:
		realchars.extend(list(comparison.split(" ")[0]))
		realchars.extend(list(comparison.split(" ")[1]))
		if comparison.split(" ")[2] == "even":
			for char in list(comparison.split(" ")[0]):
				listchars[char] = True
			for char in list(comparison.split(" ")[1]):
				listchars[char] = True
		else:
			latertosee.append(comparison)
			
	for keys,values in listchars.items():
		print(keys)
		print(values)
		
	for char in realchars:
		try:
			listchars[char]
		except:
			counterfeit = char
			if latertosee[0].split(" ")[2] == 'up' and ( char in (latertosee[0]).split(" ")[1]):
				weight = 'light.'
			else:
				weight = 'heavy.'

	print (counterfeit , 'is the counterfeit coin and it is' ,  weight)

numCases = int(input())
for i in range(numCases):
	solve()
