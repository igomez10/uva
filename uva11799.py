numcases = int(input())

for case in range(numcases):
	students = list(map(lambda x: int(x), input().split(" ")))
	print('Case', str(case+1) + ':', max(students))
		