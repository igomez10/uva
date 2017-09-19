numcases = int(input())

for i in range(numcases):
	numbers = list(map(lambda x: int(x) , input().split(' ')))
	if numbers[0] == numbers[1]:
		print('=')
		continue
	if numbers[0] > numbers[1]:
		print('>')
		pass
	else:
		print('<')